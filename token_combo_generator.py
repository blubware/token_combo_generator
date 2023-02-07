import base64, string, random
from clear_screen import clear


def token_combo_generator():
    try:
        clear()
        amount = int(input(f'Amount: '))
        generated = set()
        for _ in range(amount):
            r_first_half = ''.join(random.choice(string.digits) for _ in range(random.choice([16, 17, 18, 19, 20])))

            first_half = base64.b64encode(r_first_half.encode('utf-8')).decode().rstrip('b"')
            second_half = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            third_half = ''.join(random.choice('-' + '_' + string.ascii_letters + string.digits) for _ in range(38))
            
            whole = f'{first_half}.{second_half}.{third_half}'

            if whole not in generated:
                generated.add(whole)
                print(f'{whole}')

                with open('tokens.txt', 'a') as tokens:
                    tokens.write(f'{whole}\n')
        
        input('\nFinished, press enter to return to main menu')
        token_combo_generator()
 
    except KeyboardInterrupt:
        token_combo_generator()

if __name__ == '__main__':
    token_combo_generator()