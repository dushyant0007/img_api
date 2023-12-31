import sqlite3 
from flask import Flask, render_template, request

app = Flask(__name__)

db = sqlite3.connect("try.db",check_same_thread=False)


@app.route("/")
def index():
    return render_template("search.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        # from Lex import Lexica
        # cookie = "__Host-next-auth.csrf-token=33b753b4f3a057ada6cfbaf16b3c795e02b911f98f46123f619a0beba0d584e8%7Ccc7603feddd3bf92006af4f6573cf1e88636ab2c6b9d7b0c935e0d161355f5e9; __Secure-next-auth.callback-url=https%3A%2F%2Fz.lexica.art; _iidt=W8SKi/n64dgCNVt1FrrDOFA9kmCTjVSVhFmLps0odyE06qBn7OFMbqfMP0Zc6EVc9zSeXmH1QLsrqoVALdhNUlV+0Q==; _vid_t=gpG2VJqRPDYfdchLhT4CdHnM6JcsakOEsKtdYlIis/0FxBepvH/1TvEYVTKd3ePMfo2KfUbvE71COZ148MuBsSmEHw==; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..qLeV7fpIQqENMJcn.EVVFDJFzqReqF4SONm0aBg5tF-hHdAv_yRTRGQJUFIIAUwoSvQetIF0tQPKm8rnC06zcc-J_wvtyI71ez5UEUxNrHdAuPZ9sJPoScg_d8-p1gCTvF722t1O871vqYhc4sjMueRHEU9221LpqlHPjgl3ChhGE3mqrS3jUXG_HPcg9fxGsR9bzBr0hg_H97cfpQa-lfsUlnWln1oG3riQzhlibZG9zNMUR3ee108ncd1ey3exnK56UTiubKuMX0fBY-ngB3mEsQmz-df79P8SNur2selPj1CTRbx2AppG4DLOyJGGHYfvXYUQHFLesQqTKpBDDk_vuh6sDyFMfVsWljmKx5-aU8mvUlm6tKCVIVFdR_inmQNylDFDAYbwOIouYt0rV04XrMkbPS7sn.o9OmF5joPicbWwQnG0RaVg"
        # lex = Lexica(query=q).images()

        # --------------------------------
        # import requests

        # url = "https://api.edenai.run/v2/image/generation"

        # payload = {
        #     "resolution": "512x512",
        #     "providers": "stabilityai",
        #     "text": q,
        #     "num_images": 1
        # }
        # headers = {
        #     "accept": "application/json",
        #     "content-type": "application/json",
        #     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFhOWRjM2EtOTU5Zi00OTk0LWI0MDUtZDRkOGQzM2JmZDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.CZ1Eu4uXXATuO39s04R8L1ScnCLZ-TzOLia71hjs-BQ"
        # }

        # response = requests.post(url, json=payload, headers=headers)

        # theimg = response.json()['stabilityai']['items'][0]['image_resource_url']
        # with open('x.json',mode='w') as myfile:
        #     myfile.write(f'{theimg}')

        # print(theimg)

        # ------------------------------------------

        import requests

        url = "https://api.edenai.run/v2/image/generation"

        payload = {
            # "resolution": "256x256",
            "resolution": "1024x1024",
            "providers": "openai",
            "text": q,
            "num_images": 1
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFhOWRjM2EtOTU5Zi00OTk0LWI0MDUtZDRkOGQzM2JmZDBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.CZ1Eu4uXXATuO39s04R8L1ScnCLZ-TzOLia71hjs-BQ"
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response.json())
        theimg = response.json()['openai']['items'][0]['image_resource_url']

        # -------------------------------------

        shows = db.execute("SELECT * FROM movie_table WHERE title LIKE ? LIMIT 50",[f"%{q}%"]).fetchall()

        import httpx
        response = httpx.post("https://z.lexica.art/api/generator", headers={}, 
                              json={
            "Authorization": "yMHw4UidZM1Hha82AZtMjI50bYCfC3sdX7vvB",
            "inputText":'A pig in the style of Starry Night by Vincent Van Gogh'
        })
        print(response)

        # ----------------------------------------

    else:
        shows = []
    return render_template("search.html", shows=shows,theimg=theimg)

if __name__ == '__main__':
    print('run')