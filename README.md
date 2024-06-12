# creer un environnement virtuel python : 
'''python -m venv .venv'''
# activer l'environnementvirtuel : 
'''./.venv/Scripts/activate.bat'''
# creation d'un fichier pour stoke les bonnes version pour se projet :
 '''pip freeze > requirement.txt'''

# scrapy
'''
    pip intall scrapy
    scrapy startproject Scrapy_Brvm
    # start scrapy
    scrapy crawl brvm_spider

'''
# fastapi
'''
    pip install fastapi
    pip install "uvicorn[standard]"
    # start fast api
    uvicorn main:app --reload
'''
# os et subprocess
'''
    pip install os-sys
'''

# Deploiement
'''
    https://pereprogramming.com/articles/comment-deployer-fastapi-chez-alwaysdata/ #tuto pour alwaysdata
    https://www.alwaysdata.com/fr/ # inscription
    ssh -A krouma_raspagem@ssh-krouma.alwaysdata.net #acces a mon compte
    git clone https://github.com/IdrissaKrouma/Raspagem-api.git
    cd Raspagem-api/
    pip install fastapi[all]
    pip install schedule
    uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"



'''


     
