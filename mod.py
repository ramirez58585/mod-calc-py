    def calculate_modulo():
    print("Modulo Calculator")
    print("=" * 50)
    
    while True:
        print("\nEnter expression in format: base^exponent mod modulus")
        print("Example: 7^17 mod 10")
        print("Or type 'quit' to exit")
        
        user_input = input("\n> ").strip().lower()
        
        if user_input == 'quit':
            break
        
        try:
            if 'mod' not in user_input:
                print("Error: Please include 'mod' in your expression")
                continue
            
            parts = user_input.split('mod')
            power_part = parts[0].strip()
            modulus = int(parts[1].strip())
            
            if '^' in power_part:
                base, exponent = power_part.split('^')
                base = int(base.strip())
                exponent = int(exponent.strip())
                result = pow(base, exponent, modulus)
                print(f"\n{base}^{exponent} mod {modulus} = {result}")
            else:
                value = int(power_part)
                result = value % modulus
                print(f"\n{value} mod {modulus} = {result}")
                
        except ValueError:
            print("Error: Invalid input format")
        except ZeroDivisionError:
            print("Error: Modulus cannot be zero")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculate_modulo()
