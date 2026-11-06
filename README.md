# embedding_cpu
embedding model + torch_cpu

intfloat/multilingual-e5-large

uvx hf download cointegrated/LaBSE-en-ru --local-dir /mnt/hdd_data/@named_volumes/vllm_node/models/LaBSE-en-ru-coi

intfloat/multilingual-e5-large
uvx hf download intfloat/multilingual-e5-large --local-dir /mnt/hdd_data/@named_volumes/vllm_node/models/multilingual-e5-large

ai-forever/ru-en-RoSBERTa
uvx hf download ai-forever/ru-en-RoSBERTa --local-dir /mnt/hdd_data/@named_volumes/vllm_node/models/ai-forever/ru-en-RoSBERTa



-----
docker compose exec -it worker python -c "
import httpx, numpy as np

texts = [
    'Bolgheri Sassicaia 2014 DOC | Intense, concentré et de couleur rubis profond, ce vin offre des arômes élégants et complexes de fruits rouges. En bouche, il est riche et dense, mais harmonieux, avec des tanins doux et équilibrés. \rLe vin a une longue finale avec une profondeur et une structure qui assurent sa longévité extraordinaire. | Bolgheri Sassicaia 2014 DOC | Sassicaia, Tenuta San Guido, Bolgheri | Bolgheri Sassicaia 2014 DOC | Насыщенное, полнотелое вино, глубокого рубинового оттенка предлагает элегантные, сложные а
 оматы красных фруктов. Вино имеет богатый и плотный, но гармоничный вкус, со сладкими, сбалансированными танинами. \r+ Обладает послевкусием с глубиной и структурой, обеспечивющ
 й его необычайную продолжительность. | Intense, concentrated and deep ruby-colored, this wine offers elegant, complex aromas of red fruits. In the mouth it is rich and dense, but harmonious, with sweet, balanced tannins. \r+ The wine has a long finish with a depth and structure that ensure its extraordinary longevity. | Tenuta San Guido | Tenuta San Guido | Tenuta San Guido | Дичь | Game (venison) | Баранина | Lamb | Каберне Совиньон | Cabernet Sauvignon | Каберне Фран | Cabernet Franc | DOC | San Guido | manual | ручной ввод | Rouge | Red, Red Wine, Grenache  Garnacha  Cannonau, Amarone | Red | Красное | sequential',
    'Bolgheri Sassicaia 2014 DOC',
]             
r = httpx.post('http://embedder:8001/embed', json={'texts': texts}, timeout=60)
vecs = np.array(r.json()['vectors'], dtype=np.float32)
vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)
cos = vecs @ vecs.T
                   
for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        print(f'{cos[i,j]:.4f}  {texts[i][:30]!r:35s} <-> {texts[j][:30]!r}')
"