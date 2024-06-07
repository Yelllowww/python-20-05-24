import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1')
    print('Conexão_db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = '''CREATE DATABASE if not exists db_cadastro'''
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print("Conexão fechada")

def create_connection():
    conexao = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1',
                                        database='db_cadastro')
    print('Conexão:', conexao)
    return conexao

def create_table():
    create = '''CREATE TABLE if not exists tb_cargo(
                idt INT NOT NULL AUTO_INCREMENT,
                cargo VARCHAR(20) UNIQUE NOT NULL,
                PRIMARY KEY(idt))'''
    cursor.execute(create)

    create2 = '''CREATE TABLE if not exists funcionario(
                matricula INT NOT NULL AUTO_INCREMENT,
                nome CHAR(50) NOT NULL,
                dt_nascimento DATE,
                genero ENUM('m','f') NOT NULL,
                cd_cargo INT NOT NULL, 
                PRIMARY KEY(matricula),
                FOREIGN KEY(cd_cargo) REFERENCES tb_cargo(idt))'''
    cursor.execute(create2)

def insert_cargo():
    insere_cargo = input("Digite o cargo:")
    insert = f'''INSERT INTO tb_cargo (cargo) VALUES('{insere_cargo}')'''
    cursor.execute(insert)
    conexao.commit()
def insert_empregado():
    insere_nome = input("Digite o nome:")
    insere_data = input("Digite a data de nascimento:")
    insere_genero = input("Digite o gênero:")
    insert2 = f'''INSERT INTO funcionario(nome,dt_nascimento,genero,cd_cargo) 
                VALUES('{insere_nome}','{insere_data}','{insere_genero}',1)'''
    cursor.execute(insert2)
    conexao.commit()

def delete():
    deleta_nome = input("Digite o nome do registro a ser excluído:")
    delete = f'''DELETE FROM funcionario WHERE nome = '{deleta_nome}' '''
    cursor.execute(delete)
    conexao.commit()

def select():
    select = '''SELECT e.nome,e.dt_nascimento,e.genero,c.cargo 
    FROM funcionario as  e inner join tb_cargo as c
    WHERE e.cd_cargo = c.idt'''
    cursor.execute(select)
    registros = cursor.fetchall()
    for i in registros:
        print(i)

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada')

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    while True:
        print("\nMenu:")
        print("-Digite 1 para inserir um registro")
        print("-Digite 2 para apagar um registro")
        print("-Digite 3 para mostrar os registros")
        print("-Digite 4 para encerrar o programa")
        sinal = int(input("\ninput:"))
        if sinal == 1:
            insert_empregado()
        elif sinal == 2:
            delete()
        elif sinal == 3:
            select()
        elif sinal == 4:
            break
        else:
            print("Inserção inválida")

    close_connection()