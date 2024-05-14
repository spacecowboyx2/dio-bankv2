def menu():
    print('''

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair

>: ''')
    op = input()
    return op

def deposit(balance, value, bank_statement,/):
    if value > 0:
        balance += value  
        bank_statement += f"Depósito:\t{value:.2f} R$." 
        print("Depósito realizado com sucesso. ")

    else:
        print("Valor informado é inválido.")

    return balance, bank_statement
    

def withdraw(*, balance, value, bank_statement, limit_withdraw, withdraw_number, limit_withdraw_number):
    exceeded_balance = value > balance
    exceeded_limit = value > limit_withdraw 
    exceeded_withdrawals =  withdraw_number >= limit_withdraw_number

    if exceeded_balance:
        print("Você não tem saldo suficiente.")
    elif exceeded_limit:
        print("Você não pode sacar mais que 500 reais.")
    elif exceeded_withdrawals:
        print("Limite de saques atingido.")
    elif value > 0:
        balance -= value
        bank_statement += f"Saque:\t {value:.2f} R$ realizado."
        withdraw_number += 1
        print(f"Saque de {value} R$ realizado com sucesso.")
    else:
        print("Valor informado inválido.")
    return balance, bank_statement
        

def statement(balance, /, *, bank_statement):
    print("------Extrato-----")
    print("não foram realizadas operações bancárias." if not bank_statement else bank_statement)
    print(f"saldo: \t{balance} R$")
    print("--------------------")   

def new_account(bank_branch, account, users):
    cpf = input("cpf: ")
    user = filter_user(cpf, users)

    if user:
        print("Conta criada com sucesso.")
        return {"agência": bank_branch, "conta": account, "user": user}
    else: 
        print("você deve criar um usuário.")


def new_user(user):
    cpf = input("Digite o CPF: ")

    if filter_user(cpf, user) is not None:
        print("Usuário já existe.")
        return
    name = input("Nome: ")
    date_of_birth = input("data de Nascimento: ")
    address = input("endereço: ")
    user.append({"name": name, "cpf": cpf, "date_of_birth": date_of_birth, "address": address})
    print("Usuário criado com sucesso.")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None



def ls_account(accounts):
    for account in accounts:
        print(f"{account['agência']} \n{account['conta']} \n{account['user']}")
        print("-" * 40)

def main():
    balance = 0
    LIMIT_WITHDRAW = 500
    bank_statement = ''
    withdraw_number = 0
    LIMIT_NUMBER_WITHDRAW = 3
    users = []
    accounts = []
    BANK_BRANCH = "0001"
    while True:
        op = menu()
        if op == 'd':
            print("-----Deposito-----")
            value = float(input("Informe o valor de depósito: "))
            balance, bank_statement = deposit(balance, value, bank_statement)

        elif op == 's':
            print('-----Saque-----')
            value = float(input("informe o valor de saque: "))
            balance, bank_statement = withdraw(balance = balance,value = value, bank_statement = bank_statement, limit_withdraw = LIMIT_WITHDRAW,
            withdraw_number = withdraw_number, limit_withdraw_number = LIMIT_NUMBER_WITHDRAW)

        elif op == "e":
            statement(balance, bank_statement=bank_statement)

        elif op == "nu":
            new_user(users)

        elif op == "nc":
            account_number = len(accounts)+1
            account = new_account(BANK_BRANCH,account_number, users)
            if account:
                accounts.append(account)
        
        elif op == "lc":
            ls_account(accounts)
        
        elif op == "q":
            break
        
        else: 
            print("Comando Inválido.")

main()