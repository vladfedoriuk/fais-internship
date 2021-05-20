#include <cpr/cpr.h>
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
#include <string>
#include <vector>

struct Parameter{
    std::string param;
    std::string valid_from;
    std::string valid_to;
    std::size_t version;
};

using namespace rapidjson;

void getRunContainer(long runid, unsigned long version){
    cpr::Response r = cpr::Get(cpr::Url{"127.0.0.1:9081/api/retrieve/" + std::to_string(runid)},
                            cpr::Header{{"Authorization", "Token b80052ba3fbb02b93792105ab9aed5ce9d723cb4"}},
                            cpr::Parameters{{"version", std::to_string(version)}});
    
    if( r.status_code >= 200 && r.status_code < 400){
        const char* json = r.text.c_str();
        Document d;
        d.Parse(json);
        if(d.HasMember("data")){
            const Value& data = d["data"];
            for (Value::ConstMemberIterator itr = data.MemberBegin(); itr != data.MemberEnd(); ++itr){
                std::cout << itr->name.GetString() << std::endl;
                const Value& params_list = itr->value;
                std::cout << params_list[0]["parameters"].GetString() << std::endl;
            }
        }
    }               
    //dopytać o kolejność.
}

std::map<std::string, Parameter> getRunContainers(long min_runid, long max_runid){
    cpr::Response r = cpr::Get(cpr::Url{"127.0.0.1:9081/api/retrieve/" + std::to_string(min_runid)} + "/" + std::to_string(max_runid),
                            cpr::Header{{"Authorization", "Token b80052ba3fbb02b93792105ab9aed5ce9d723cb4"}});
    if( r.status_code >= 200 && r.status_code < 400){
        const char* json = r.text.c_str();
        std::map<std::string, Parameter> map;
        Document d;
        d.Parse(json);
        if(d.HasMember("data")){
            const Value& data = d["data"];
            for (Value::ConstMemberIterator itr = data.MemberBegin(); itr != data.MemberEnd(); ++itr){
                std::string name = std::string(itr->name.GetString(), itr->name.GetStringLength());
                const Value& params_list = itr->value;
                Parameter p;
                int max_version = -1;
                int current_version;
                for (auto& v : params_list.GetArray()){
                    current_version = (int) v["version"].GetInt();
                    if (current_version > max_version){
                        max_version = current_version;
                        p.version = max_version;
                        p.param = std::string(v["parameters"].GetString(), v["parameters"].GetStringLength());
                        p.valid_from = std::string(v["valid_from"].GetString(), v["valid_from"].GetStringLength());
                        p.valid_to = std::string(v["valid_to"].GetString(), v["valid_to"].GetStringLength());
                    }
                }
                map[name] = p;
            }
        }
        return std::move(map);            
    }  
}


int main(int argc, char** argv) {
    //getRunContainer(1, 1);
    auto m = getRunContainers(1, 2);
    for (const auto& [key, value] : m) {
        std::cout << key << std::endl;
        std::cout << value.version << std::endl;
    }
    return 0;
}