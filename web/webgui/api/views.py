from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import get_serializer, ReleaseSerializer
from django.apps import apps
from core.models import Configuration, Files
from . import utils
from .utils.codes import ResponseData
from rest_framework import status
from collections import defaultdict
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

version_param = openapi.Parameter(
    'version', 
    openapi.IN_QUERY, 
    description="The version of the parameters.",
    type=openapi.TYPE_INTEGER
)

class ConfigurationsView(APIView):   
    
         
    @swagger_auto_schema(
        manual_parameters=[version_param],
        responses={
            404: utils.codes.CODE_404.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        }     
    )
    def get(self, request, run_id):
        core_models = apps.get_app_config('core').get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))
        
        run = Files.objects.filter(run_id=run_id)
        if not run:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_404_NOT_FOUND,
                    code=utils.codes.CODE_404._asdict(),
                    message=f'The run with run_id={run_id} was not found.',
                    errors = [],
                    data=None
                )._asdict(),
                status=status.HTTP_404_NOT_FOUND
            )
        run = run.first()
        
        version = request.query_params.get('version')
        if version:
            version = int(version) 
            
        conf_json = defaultdict(list)
        for conf_model in core_models:
            serializer = get_serializer(conf_model)
            confs = conf_model.objects.filter(
                valid_from__lte=run.start_time,
                valid_to__gte=run.stop_time
            ).all()
            confs = serializer(confs, many=True)
            
            if version:
                versions = [x['version'] for x in confs.data]
                
                if version not in versions:
                    return Response(
                        data=ResponseData(
                            http_status=status.HTTP_404_NOT_FOUND,
                            code=utils.codes.CODE_404._asdict(),
                            message=f'The version {version} was not found in one or more the tables.',
                            errors = [],
                            data=None
                        )._asdict(),
                        status=status.HTTP_404_NOT_FOUND
                    )
                else:
                    confs = [x for x in confs.data if x['version'] == version]
            else:
                confs = [x for x in confs.data]
                
            if not confs:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message='Some of the configuration parameters do not exist.',
                        errors = [],
                        data=None
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT
                )
                
            conf_json[serializer.model_name()].extend(confs)
            
        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message='OK.',
                    errors = [],
                    data=None
                )._asdict(),
                status=status.HTTP_204_NO_CONTENT
            )
          
        return Response(
            data=ResponseData(
                http_status=status.HTTP_200_OK,
                code=utils.codes.CODE_200._asdict(),
                message='OK',
                errors = [],
                data=conf_json
            )._asdict(),
            status=status.HTTP_200_OK
        )
        
        
            
        
        