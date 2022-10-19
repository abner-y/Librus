Essa é a ferramenta LIBRUS, uma ferramenta lúdica e interativa em python
que se utiliza de bibliotecas como kivy por exemplo, para ajudar
no manuseio de casos investigativos e seus respectivos documentos(anexos).

Para ajustar corretamente é necessário a alteração nas conexões com o banco de dados
em arquivos como em main.py, crudAnexos, crudCasos, casosPagina e primeiraPagina,
e também o caminho de arquivo de seu diretório pessoal, em arquivos como arquivos.py
por exemplo.

Para criação das tabelas no banco de dados segue o código sql abaixo:

CREATE TABLE casos (
    idcasos INT PRIMARY KEY AUTO_INCREMENT,
    nomeCaso VARCHAR(100) COLLATE utf8_general_ci,
    descricao MEDIUMTEXT COLLATE utf8_general_ci,
    fotoCaso VARCHAR(100) COLLATE utf8_general_ci,
    dataCriacao DATETIME,
    dataEdit DATETIME,
    autor VARCHAR(100)
);

CREATE TABLE anexos (
    idAnexo INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    tipo VARCHAR(20),
    dataCriacao DATETIME,
    casosRelacionados VARCHAR(300),
    autor VARCHAR(100),
    idcasos INT,
    FOREIGN KEY(idcasos) REFERENCES casos(idcasos) ON DELETE CASCADE
);

E por fim também é necessário criar a pasta casos para que seja feito o armazenamento
de anexos ligados a cada caso.