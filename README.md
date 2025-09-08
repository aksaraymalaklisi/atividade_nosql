# Repositório da Atividade Avaliativa 1 - P1

O arquivo `example.env` contém uma .env de exemplo. Os valores padrões inseridos no settings.py já devem ser suficientes em rede local.  
Caso contrário, configure de acordo.  

Por simplicidade, o código não cobre os métodos CRUD com sufixo "_many", apenas os com "_one".
A razão para isso é o funcionamento muito similar deles. Além de não haver nada especificando o uso desses métodos.

---

Foram utilizados 4 métodos do MongoClient que permitem manipular a collection:

`insert_one(documento)`  
Recebe um documento (dict) e insere-o na database. Esse método também retorna o ID do documento criado.

`find_one(filter, projection=None)`
Recebe um documento (dict) que é utilizado como filtro de busca. projection, por padrão, está vazio. Ele define que campos serão retornados usando booleanos. Ex.: {"nome":1, "idade":False}

`update_one(filter, update, upsert=False)`
Recebe um dict como filtro de busca e, no segundo argumento, um dict contendo a mudança requisitada. O segundo argumento DEVE CONTER UM OPERADOR do MongoDB. Ex.: {"$set": {"nome":"Carlos"}}.  

Já o upsert, se for verdadeiro (falso por padrão), irá INSERIR o documento usando o filter como base SE o documento procurado não existir. Ele também retorna um objeto chamado (UpdateResult). Ele possui alguns atributos úteis, como matched_count, modified_count. Se você usou o upsert, ele também manda o id do documento adicionado no atributo upserted_id.

`delete_one(filter)`  
Similar ao find_one, mas APAGA o documento encontrado. Ele retorna um objeto chamado DeleteResult. Ele possui um atributo chamado deleted_count, que diz a quantidade de documentos apagados. deleted_count não é tão útil aqui porque apenas um documento é deletado com o delete_one.  
Naturalmente, há outros atributos, (como o ObjectID).
