import requests #pip install requestsなどが必要　HTTPリクエストを簡単に行うためのものです

#GETメソッドによる天気予報APIを使用し土浦市の今日の天気予報を取得するプログラム
class TuchiuraWeather(object):
    def get_todays_forecast(self):
        try:#今日の天気予報を取得し、その結果を返します
            return self._fetch()['forecasts'][0]['telop']
        except Exception:#_fetch()メソッドが天気予報の取得に失敗した場合WetherFetchErrorをスローする
            raise WeatherFetchError()
    
    def _fetch(self):#天気予報APIに対してHTTP GETリクエストを送信し、JSON形式で受け取った結果を返します。
        return requests.\
            get('https://weather.tsukumijima.net/api/forecast/city/080020').\
            json()

if __name__ == '__main__':
    print("土浦の今日の天気予報は：")
    #TuchiuraWeatherのインスタンスを作成し、get_todays_forecast()メソッドを呼び出して、土浦市の今日の天気予報を取得し、出力します。
    print(TuchiuraWeather().get_todays_forecast())
