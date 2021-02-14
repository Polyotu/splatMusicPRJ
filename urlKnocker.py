import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import json
import os
import codecs
import random
import pprint

#myModule
import iksmXmlReader as iksmXml

# 引数のURL(Splatoon API)にアクセス、レスポンスのJSONデータをreturn
def getJson(url): # UrlにアクセスしJsonを取得
    print("api access")
    cookie = "iksm_session="+str(iksmXml.tokenFromXml('D:/Users/poly_Z/Documents/splatmusicprj/streamingWidget/data/config.xml'))#"4eb6aaef97beaee255673387d5c0d5173e51fe17"
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    opener.addheaders.append(("Cookie", cookie))
    # print(url)
    res = opener.open(url)
    # print(res)
    return json.load(res)

# 引数のJSONデータ(戦績データを期待)を戦績ごとにファイルに保存
def saveButtleResults(jsonData):
    for result in jsonData["results"]:
        # この戦績に対応するファイル名とパスを組み立てる
        outputFilePath = "保存先のパス/result-buttle-" + result["battle_number"] + ".json"
        # この戦績ファイルが既に存在するか確認、なかったら作成・書き込み
        if not(os.path.exists(outputFilePath)) :
            outputFile = codecs.open(outputFilePath, "w", encoding="utf-8")
            json.dump(result, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
            outputFile.close()

def saveSingleResult(jsonData):
    outputFilePath = "D:/Users/poly_Z/Documents/splatmusicprj/test1.json"
    outputFile = codecs.open(outputFilePath, "w", encoding="utf-8")
    json.dump(jsonData, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
    outputFile.close()

#バトルログ50戦から最新バトルの番号を返す
def getNewestButtleNumber(jsonData):
    for result in jsonData["results"]:
        num=result["battle_number"]
        break
    return num

#固定jsonファイルでの試運転用
def readTemplateJson():
    json_open = open('D:/Users/poly_Z/Documents/splatmusicprj/test'+str(random.randint(0,2))+'.json','r',encoding="utf-8")
    json_load = json.load(json_open)
    return json_load


#任意の1戦のログから対戦成績のリストを作成して返す
def getNewestButtleResult(jsonData):
    d={}
    c=-1
    if(jsonData["type"]=="league"):#リグマ
        d={
            "mode"      :jsonData["game_mode"]["name"],
            "rule"      :jsonData["rule"]["name"],
            "stage"     :jsonData["stage"]["name"],
            "vicordef"  :jsonData["my_team_result"]["name"],
            "ourcount"  :jsonData["my_team_count"],
            "enemycount":jsonData["other_team_count"],
            "ourmaxlp"  :jsonData["max_league_point"],
            "ourlp"     :jsonData["league_point"],
            "enemylp"   :jsonData["other_estimate_league_point"],
            "ourlog":[
                {
                    "name":jsonData["player_result"]["player"]["nickname"],
                    "kill":jsonData["player_result"]["kill_count"],
                    "assist":jsonData["player_result"]["assist_count"],
                    "death":jsonData["player_result"]["death_count"],
                    "sp":jsonData["player_result"]["special_count"],
                    "paint":jsonData["player_result"]["game_paint_point"],
                    "weapon":jsonData["player_result"]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][0]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][0]["kill_count"],
                    "assist":jsonData["my_team_members"][0]["assist_count"],
                    "death" :jsonData["my_team_members"][0]["death_count"],
                    "sp"    :jsonData["my_team_members"][0]["special_count"],
                    "paint" :jsonData["my_team_members"][0]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][0]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][1]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][1]["kill_count"],
                    "assist":jsonData["my_team_members"][1]["assist_count"],
                    "death" :jsonData["my_team_members"][1]["death_count"],
                    "sp"    :jsonData["my_team_members"][1]["special_count"],
                    "paint" :jsonData["my_team_members"][1]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][1]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][2]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][2]["kill_count"],
                    "assist":jsonData["my_team_members"][2]["assist_count"],
                    "death" :jsonData["my_team_members"][2]["death_count"],
                    "sp"    :jsonData["my_team_members"][2]["special_count"],
                    "paint" :jsonData["my_team_members"][2]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][2]["player"]["weapon"]["name"]
                }
            ],
            "enemylog":[
                {
                    "name"  :jsonData["other_team_members"][0]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][0]["kill_count"],
                    "assist":jsonData["other_team_members"][0]["assist_count"],
                    "death" :jsonData["other_team_members"][0]["death_count"],
                    "sp"    :jsonData["other_team_members"][0]["special_count"],
                    "paint" :jsonData["other_team_members"][0]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][0]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][1]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][1]["kill_count"],
                    "assist":jsonData["other_team_members"][1]["assist_count"],
                    "death" :jsonData["other_team_members"][1]["death_count"],
                    "sp"    :jsonData["other_team_members"][1]["special_count"],
                    "paint" :jsonData["other_team_members"][1]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][1]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][2]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][2]["kill_count"],
                    "assist":jsonData["other_team_members"][2]["assist_count"],
                    "death" :jsonData["other_team_members"][2]["death_count"],
                    "sp"    :jsonData["other_team_members"][2]["special_count"],
                    "paint" :jsonData["other_team_members"][2]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][2]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][3]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][3]["kill_count"],
                    "assist":jsonData["other_team_members"][3]["assist_count"],
                    "death" :jsonData["other_team_members"][3]["death_count"],
                    "sp"    :jsonData["other_team_members"][3]["special_count"],
                    "paint" :jsonData["other_team_members"][3]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][3]["player"]["weapon"]["name"]
                },
            ]
        }
        c=0
    elif(jsonData["game_mode"]["key"]=="private"):#プラベ
        if(jsonData["type"]=="gachi"):#ガチルール
            d={
                "mode"      :jsonData["game_mode"]["name"],
                "rule"      :jsonData["rule"]["name"],
                "stage"     :jsonData["stage"]["name"],
                "vicordef"  :jsonData["my_team_result"]["name"],
                "ourcount"  :jsonData["my_team_count"],
                "enemycount":jsonData["other_team_count"],
                "ourlog":[
                    {
                        "name":jsonData["player_result"]["player"]["nickname"],
                        "kill":jsonData["player_result"]["kill_count"],
                        "assist":jsonData["player_result"]["assist_count"],
                        "death":jsonData["player_result"]["death_count"],
                        "sp":jsonData["player_result"]["special_count"],
                        "paint":jsonData["player_result"]["game_paint_point"],
                        "weapon":jsonData["player_result"]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][0]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][0]["kill_count"],
                        "assist":jsonData["my_team_members"][0]["assist_count"],
                        "death" :jsonData["my_team_members"][0]["death_count"],
                        "sp"    :jsonData["my_team_members"][0]["special_count"],
                        "paint" :jsonData["my_team_members"][0]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][0]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][1]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][1]["kill_count"],
                        "assist":jsonData["my_team_members"][1]["assist_count"],
                        "death" :jsonData["my_team_members"][1]["death_count"],
                        "sp"    :jsonData["my_team_members"][1]["special_count"],
                        "paint" :jsonData["my_team_members"][1]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][1]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][2]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][2]["kill_count"],
                        "assist":jsonData["my_team_members"][2]["assist_count"],
                        "death" :jsonData["my_team_members"][2]["death_count"],
                        "sp"    :jsonData["my_team_members"][2]["special_count"],
                        "paint" :jsonData["my_team_members"][2]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][2]["player"]["weapon"]["name"]
                    }
                ],
                "enemylog":[
                    {
                        "name"  :jsonData["other_team_members"][0]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][0]["kill_count"],
                        "assist":jsonData["other_team_members"][0]["assist_count"],
                        "death" :jsonData["other_team_members"][0]["death_count"],
                        "sp"    :jsonData["other_team_members"][0]["special_count"],
                        "paint" :jsonData["other_team_members"][0]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][0]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][1]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][1]["kill_count"],
                        "assist":jsonData["other_team_members"][1]["assist_count"],
                        "death" :jsonData["other_team_members"][1]["death_count"],
                        "sp"    :jsonData["other_team_members"][1]["special_count"],
                        "paint" :jsonData["other_team_members"][1]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][1]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][2]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][2]["kill_count"],
                        "assist":jsonData["other_team_members"][2]["assist_count"],
                        "death" :jsonData["other_team_members"][2]["death_count"],
                        "sp"    :jsonData["other_team_members"][2]["special_count"],
                        "paint" :jsonData["other_team_members"][2]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][2]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][3]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][3]["kill_count"],
                        "assist":jsonData["other_team_members"][3]["assist_count"],
                        "death" :jsonData["other_team_members"][3]["death_count"],
                        "sp"    :jsonData["other_team_members"][3]["special_count"],
                        "paint" :jsonData["other_team_members"][3]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][3]["player"]["weapon"]["name"]
                    },
                ]
            }
            c=1
        elif(jsonData["type"]=="regular"):#ナワバリルール
            d={
                "mode"      :jsonData["game_mode"]["name"],
                "rule"      :jsonData["rule"]["name"],
                "stage"     :jsonData["stage"]["name"],
                "vicordef"  :jsonData["my_team_result"]["name"],
                "ourpaint"  :jsonData["my_team_percentage"],
                "enemypaint":jsonData["other_team_percentage"],
                "ourlog":[
                    {
                        "name":jsonData["player_result"]["player"]["nickname"],
                        "kill":jsonData["player_result"]["kill_count"],
                        "assist":jsonData["player_result"]["assist_count"],
                        "death":jsonData["player_result"]["death_count"],
                        "sp":jsonData["player_result"]["special_count"],
                        "paint":jsonData["player_result"]["game_paint_point"],
                        "weapon":jsonData["player_result"]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][0]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][0]["kill_count"],
                        "assist":jsonData["my_team_members"][0]["assist_count"],
                        "death" :jsonData["my_team_members"][0]["death_count"],
                        "sp"    :jsonData["my_team_members"][0]["special_count"],
                        "paint" :jsonData["my_team_members"][0]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][0]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][1]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][1]["kill_count"],
                        "assist":jsonData["my_team_members"][1]["assist_count"],
                        "death" :jsonData["my_team_members"][1]["death_count"],
                        "sp"    :jsonData["my_team_members"][1]["special_count"],
                        "paint" :jsonData["my_team_members"][1]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][1]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["my_team_members"][2]["player"]["nickname"],
                        "kill"  :jsonData["my_team_members"][2]["kill_count"],
                        "assist":jsonData["my_team_members"][2]["assist_count"],
                        "death" :jsonData["my_team_members"][2]["death_count"],
                        "sp"    :jsonData["my_team_members"][2]["special_count"],
                        "paint" :jsonData["my_team_members"][2]["game_paint_point"],
                        "weapon":jsonData["my_team_members"][2]["player"]["weapon"]["name"]
                    }
                ],
                "enemylog":[
                    {
                        "name"  :jsonData["other_team_members"][0]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][0]["kill_count"],
                        "assist":jsonData["other_team_members"][0]["assist_count"],
                        "death" :jsonData["other_team_members"][0]["death_count"],
                        "sp"    :jsonData["other_team_members"][0]["special_count"],
                        "paint" :jsonData["other_team_members"][0]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][0]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][1]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][1]["kill_count"],
                        "assist":jsonData["other_team_members"][1]["assist_count"],
                        "death" :jsonData["other_team_members"][1]["death_count"],
                        "sp"    :jsonData["other_team_members"][1]["special_count"],
                        "paint" :jsonData["other_team_members"][1]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][1]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][2]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][2]["kill_count"],
                        "assist":jsonData["other_team_members"][2]["assist_count"],
                        "death" :jsonData["other_team_members"][2]["death_count"],
                        "sp"    :jsonData["other_team_members"][2]["special_count"],
                        "paint" :jsonData["other_team_members"][2]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][2]["player"]["weapon"]["name"]
                    },
                    {
                        "name"  :jsonData["other_team_members"][3]["player"]["nickname"],
                        "kill"  :jsonData["other_team_members"][3]["kill_count"],
                        "assist":jsonData["other_team_members"][3]["assist_count"],
                        "death" :jsonData["other_team_members"][3]["death_count"],
                        "sp"    :jsonData["other_team_members"][3]["special_count"],
                        "paint" :jsonData["other_team_members"][3]["game_paint_point"],
                        "weapon":jsonData["other_team_members"][3]["player"]["weapon"]["name"]
                    },
                ]
            }
            c=2
    elif(jsonData["game_mode"]["key"]=="regular"):#ナワバリ
        d={
            "mode"      :jsonData["game_mode"]["name"],
            "rule"      :jsonData["rule"]["name"],
            "stage"     :jsonData["stage"]["name"],
            "vicordef"  :jsonData["my_team_result"]["name"],
            "ourpaint"  :jsonData["my_team_percentage"],
            "enemypaint":jsonData["other_team_percentage"],
            "ourlog":[
                {
                    "name":jsonData["player_result"]["player"]["nickname"],
                    "kill":jsonData["player_result"]["kill_count"],
                    "assist":jsonData["player_result"]["assist_count"],
                    "death":jsonData["player_result"]["death_count"],
                    "sp":jsonData["player_result"]["special_count"],
                    "paint":jsonData["player_result"]["game_paint_point"],
                    "weapon":jsonData["player_result"]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][0]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][0]["kill_count"],
                    "assist":jsonData["my_team_members"][0]["assist_count"],
                    "death" :jsonData["my_team_members"][0]["death_count"],
                    "sp"    :jsonData["my_team_members"][0]["special_count"],
                    "paint" :jsonData["my_team_members"][0]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][0]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][1]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][1]["kill_count"],
                    "assist":jsonData["my_team_members"][1]["assist_count"],
                    "death" :jsonData["my_team_members"][1]["death_count"],
                    "sp"    :jsonData["my_team_members"][1]["special_count"],
                    "paint" :jsonData["my_team_members"][1]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][1]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["my_team_members"][2]["player"]["nickname"],
                    "kill"  :jsonData["my_team_members"][2]["kill_count"],
                    "assist":jsonData["my_team_members"][2]["assist_count"],
                    "death" :jsonData["my_team_members"][2]["death_count"],
                    "sp"    :jsonData["my_team_members"][2]["special_count"],
                    "paint" :jsonData["my_team_members"][2]["game_paint_point"],
                    "weapon":jsonData["my_team_members"][2]["player"]["weapon"]["name"]
                }
            ],
            "enemylog":[
                {
                    "name"  :jsonData["other_team_members"][0]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][0]["kill_count"],
                    "assist":jsonData["other_team_members"][0]["assist_count"],
                    "death" :jsonData["other_team_members"][0]["death_count"],
                    "sp"    :jsonData["other_team_members"][0]["special_count"],
                    "paint" :jsonData["other_team_members"][0]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][0]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][1]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][1]["kill_count"],
                    "assist":jsonData["other_team_members"][1]["assist_count"],
                    "death" :jsonData["other_team_members"][1]["death_count"],
                    "sp"    :jsonData["other_team_members"][1]["special_count"],
                    "paint" :jsonData["other_team_members"][1]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][1]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][2]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][2]["kill_count"],
                    "assist":jsonData["other_team_members"][2]["assist_count"],
                    "death" :jsonData["other_team_members"][2]["death_count"],
                    "sp"    :jsonData["other_team_members"][2]["special_count"],
                    "paint" :jsonData["other_team_members"][2]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][2]["player"]["weapon"]["name"]
                },
                {
                    "name"  :jsonData["other_team_members"][3]["player"]["nickname"],
                    "kill"  :jsonData["other_team_members"][3]["kill_count"],
                    "assist":jsonData["other_team_members"][3]["assist_count"],
                    "death" :jsonData["other_team_members"][3]["death_count"],
                    "sp"    :jsonData["other_team_members"][3]["special_count"],
                    "paint" :jsonData["other_team_members"][3]["game_paint_point"],
                    "weapon":jsonData["other_team_members"][3]["player"]["weapon"]["name"]
                },
            ]
        }
        c=3
    return d,c


if __name__=='__main__':
    # 多分こっちと同様のコードを実行すれば最新試合の戦績を読み込んでリスト返却ができる
    # num=getNewestButtleNumber(getJson("https://app.splatoon2.nintendo.net/api/results"))
    # print(num)
    # getNewestButtleResult(getJson("https://app.splatoon2.nintendo.net/api/results/"+str(getNewestButtleNumber(getJson("https://app.splatoon2.nintendo.net/api/results")))))

    # saveSingleResult(getJson("https://app.splatoon2.nintendo.net/api/results/17530"))

    #こっちはAPI叩きすぎ防止用，すでにPCに保存済みの過去の戦績データから適当に取得
    dic,rule=getNewestButtleResult(readTemplateJson())
    pprint.pprint(dic)