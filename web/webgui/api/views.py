from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import get_serializer, ReleaseSerializer
from django.apps import apps
from core.models import Configuration, Files
from . import utils
from .utils.codes import ResponseData
from rest_framework import status


class ConfigurationsView(APIView):        
    
    def get(self, request, run_id):
        core_models = apps.get_app_config('core').get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))

        run = Files.objects.filter(run_id=run_id)
        if not run:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_400_BAD_REQUEST,
                    code=utils.codes.CODE_405._asdict(),
                    message=f'The run with run_id={run_id} was not found.',
                    errors = [],
                    data=None
                )._asdict(),
                status=status.HTTP_400_BAD_REQUEST
            )
        run = run.first()
            
        conf_json = list()
        for conf_model in core_models:
            serializer = get_serializer(conf_model)
            confs = conf_model.objects.filter(
                valid_from__lte=run.start_time,
                valid_to__gte=run.stop_time
            ).all()
            confs = serializer(confs, many=True)
            conf_json.extend(x for x in confs.data)
            
        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message='OK',
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
        
        
            
        
        