echo "Démarrage du scraping..."
scrapy crawl brvm_spider -O top5_data.json
# cp -v top5_data.json ../fastapi_app/top5_data.json
echo "Scraping terminé."