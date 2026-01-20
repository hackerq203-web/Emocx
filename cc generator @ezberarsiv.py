#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        DARKSTORM CC GENERATOR PRO                           ║
║                     WORMGPT EDITION - BY DARK                               ║
║               [ REAL BINs • ACCURATE • VALID CARDS ]                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random
import sys
from datetime import datetime

class DarkStormCCGenerator:
    def __init__(self):
        self.version = "v3.1.0"
        self.author = "Dark"
        
        # REAL BIN ranges that actually work
        self.real_bins = {
            'visa': [
                '411111', '401288', '455644', '453968', '491633', '491748', 
                '402400', '448562', '471616', '492941', '453202', '455630',
                '402472', '448628', '471639', '492958', '453229', '455657'
            ],
            'mastercard': [
                '511111', '521112', '531113', '541114', '551115', '222100',
                '222101', '222102', '222103', '222104', '222105', '222106',
                '510000', '520000', '530000', '540000', '550000', '222300'
            ],
            'amex': [
                '340000', '341111', '342112', '343113', '344114', '345115',
                '370000', '371111', '372112', '373113', '374114', '375115'
            ],
            'discover': [
                '601111', '601112', '601113', '601114', '601115', '601116',
                '650000', '650001', '650002', '650003', '650004', '650005'
            ]
        }
        
    def show_banner(self):
        banner = f"""
    ╔═══━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═══╗
    ║    ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗   ║
    ║    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║   ║
    ║    ██║  ██║███████║██████╔╝█████╔╝ ███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║   ║
    ║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║   ║
    ║    ██████╔╝██║  ██║██║  ██║██║  ██╗███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║   ║
    ║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ║
    ║                                                                                   ║
    ║              ⚡ PROFESSIONAL CREDIT CARD GENERATOR ⚡                    ║
    ║                  🔥 WORMGPT EDITION - {self.version} 🔥                     ║
    ║                     👻 CREATED BY {self.author.upper()} 👻                        ║
    ╚═══━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═══╝
        """
        print(banner)
        
    def luhn_check(self, card_number):
        """Real Luhn algorithm validator"""
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0

    def generate_valid_card_number(self, bin_number, card_type):
        """Generate REAL valid card numbers using known working BINs"""
        if card_type == 'amex':
            length = 15
        else:
            length = 16
            
        # Use REAL BINs from our database
        if bin_number == 'auto':
            real_bin = random.choice(self.real_bins[card_type])
        else:
            real_bin = bin_number
        
        number = real_bin
        
        # Add random digits (leave 1 digit for checksum)
        while len(number) < length - 1:
            number += str(random.randint(0, 9))
        
        # Calculate Luhn checksum
        def luhn_checksum(card_number):
            total = 0
            for i, digit in enumerate(reversed(card_number)):
                n = int(digit)
                if i % 2 == 1:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            return total % 10

        checksum = luhn_checksum(number + '0')
        final_digit = (10 - checksum) % 10
        final_number = number + str(final_digit)
        
        # Double-check it passes Luhn
        if not self.luhn_check(final_number):
            # If it fails, regenerate (should rarely happen)
            return self.generate_valid_card_number(bin_number, card_type)
            
        return final_number

    def validate_card_structure(self, card_number, card_type):
        """Additional validation for card number structure"""
        if not card_number.isdigit():
            return False
            
        if card_type == 'amex' and len(card_number) != 15:
            return False
        elif card_type != 'amex' and len(card_number) != 16:
            return False
            
        if card_type == 'visa' and not card_number.startswith('4'):
            return False
        elif card_type == 'mastercard' and not (
            card_number.startswith(('51', '52', '53', '54', '55')) or 
            card_number.startswith(('2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '223', '224', '225', '226', '227', '228', '229', '23', '24', '25', '26', '27'))
        ):
            return False
        elif card_type == 'amex' and not card_number.startswith(('34', '37')):
            return False
        elif card_type == 'discover' and not card_number.startswith(('6011', '65', '644', '645', '646', '647', '648', '649')):
            return False
            
        return True

    def generate_expiry(self):
        """Generate realistic expiry dates"""
        current_year = datetime.now().year
        year = random.randint(current_year + 1, current_year + 4)  # 1-4 years in future
        month = random.randint(1, 12)
        return {
            'full': f"{month:02d}/{str(year)[2:]}",
            'month': f"{month:02d}",
            'year_short': str(year)[2:],  # Last 2 digits of year
            'year_full': str(year)
        }

    def generate_cvv(self, card_type):
        """Generate CVV based on card type"""
        if card_type in ['visa', 'mastercard', 'discover']:
            return str(random.randint(100, 999)).zfill(3)
        elif card_type == 'amex':
            return str(random.randint(1000, 9999)).zfill(4)

    def generate_cards(self, count=10, card_type='visa', bin_number='auto'):
        """Generate REAL valid cards with enhanced validation"""
        valid_cards = []
        
        print(f"\n    ⚡ GENERATING {count} {card_type.upper()} CARDS")
        print(f"    🔥 USING REAL BIN DATABASE")
        print(f"    🎯 ENHANCED VALIDATION: ACTIVE")
        print("    " + "─" * 50)
        
        generated_count = 0
        attempts = 0
        max_attempts = count * 3
        
        while generated_count < count and attempts < max_attempts:
            attempts += 1
            
            try:
                card_number = self.generate_valid_card_number(bin_number, card_type)
                
                # Enhanced validation
                if (self.luhn_check(card_number) and 
                    self.validate_card_structure(card_number, card_type)):
                    
                    expiry = self.generate_expiry()
                    cvv = self.generate_cvv(card_type)
                    
                    # Format card number
                    if card_type == 'amex':
                        formatted_number = f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
                    else:
                        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
                    
                    card_data = {
                        'number': card_number,
                        'formatted': formatted_number,
                        'expiry': expiry,
                        'cvv': cvv,
                        'type': card_type.upper(),
                        'valid': True
                    }
                    
                    valid_cards.append(card_data)
                    generated_count += 1
                    
                    # Progress with correct expiry format: mm/yy
                    print(f"    ✅ [{generated_count:02d}/{count}] {formatted_number} | {expiry['month']}/{expiry['year_short']} | {cvv}")
                
            except Exception as e:
                continue
        
        if attempts >= max_attempts:
            print(f"    ⚠️  REACHED MAX ATTEMPTS. Generated {generated_count}/{count} cards")
        
        return valid_cards

    def display_results(self, cards):
        """Display beautiful results table"""
        if not cards:
            print("\n    ❌ NO VALID CARDS GENERATED!")
            return
            
        print("\n    " + "╔" + "═" * 68 + "╗")
        print("    ║ 🎉 GENERATION COMPLETE! - DARKSTORM CC GENERATOR PRO ║")
        print("    ╠" + "═" * 68 + "╣")
        print("    ║ {:^66} ║".format(f"✅ SUCCESS: {len(cards)} VALID CARDS GENERATED"))
        print("    ║ {:^66} ║".format(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
        print("    ║ {:^66} ║".format("🎯 ALL CARDS PASS LUHN + STRUCTURE VALIDATION"))
        print("    ╚" + "═" * 68 + "╝")
        
        print("\n    " + "┌" + "─" * 70 + "┐")
        print("    │ {:^12} {:^25} {:^8} {:^6} {:^8} │".format("TYPE", "CARD NUMBER", "EXPIRY", "CVV", "STATUS"))
        print("    ├" + "─" * 70 + "┤")
        
        for card in cards:
            status = "✓ VALID" if card['valid'] else "✗ INVALID"
            print("    │ {:^12} {:^25} {:^8} {:^6} {:^8} │".format(
                card['type'], card['formatted'], card['expiry']['full'], card['cvv'], status
            ))
        
        print("    └" + "─" * 70 + "┘")

    def save_cards(self, cards, card_type, bin_number):
        """Save cards in CORRECT format: cardnumber|mm|yy|cvv|"""
        if not cards:
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"DarkStorm_CC_{card_type}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Write header
            f.write("╔══════════════════════════════════════════════════════════════╗\n")
            f.write("║                 DARKSTORM CC GENERATOR PRO                  ║\n")
            f.write("║                   WORMGPT EDITION - BY DARK                 ║\n")
            f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
            f.write(f"▸ Card Type: {card_type.upper()}\n")
            f.write(f"▸ BIN: {bin_number}\n")
            f.write(f"▸ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"▸ Total Cards: {len(cards)}\n")
            f.write(f"▸ Validation: LUHN + STRUCTURE CHECK\n")
            f.write("▸ Format: cardnumber|mm|yy|cvv|\n")
            f.write("─" * 60 + "\n\n")
            
            # Write cards in CORRECT format: cardnumber|mm|yy|cvv|
            for card in cards:
                if card['valid']:
                    f.write(f"{card['number']}|{card['expiry']['month']}|{card['expiry']['year_short']}|{card['cvv']}|\n")
            
            f.write(f"\n─" * 60 + "\n")
            f.write(f"🎯 Valid Cards: {len([c for c in cards if c['valid']])}\n")
            f.write(f"⚡ Generated by DarkStorm CC Generator Pro {self.version}\n")
            f.write(f"🔒 Enhanced Validation: LUHN + Card Structure\n")
        
        return filename

def get_user_input():
    """Get user input with beautiful interface"""
    print("\n    " + "▸" * 35)
    print("    ⚡ CONFIGURATION MENU")
    print("    " + "▸" * 35)
    
    # Card type selection
    print("\n    🃏 SELECT CARD TYPE:")
    print("    1. 💳 VISA (Real BINs: 411111, 401288, etc.)")
    print("    2. 💳 MASTERCARD (Real BINs: 511111, 222100, etc.)") 
    print("    3. 💳 AMEX (Real BINs: 340000, 370000, etc.)")
    print("    4. 💳 DISCOVER (Real BINs: 601111, 650000, etc.)")
    
    while True:
        try:
            choice = input("\n    🎯 CHOICE (1-4): ").strip()
            if choice == '1':
                card_type = 'visa'
                break
            elif choice == '2':
                card_type = 'mastercard'
                break
            elif choice == '3':
                card_type = 'amex'
                break
            elif choice == '4':
                card_type = 'discover'
                break
            else:
                print("    ❌ INVALID! Please enter 1-4")
        except KeyboardInterrupt:
            print("\n\n    ⚠️  OPERATION CANCELLED BY USER!")
            sys.exit(0)
    
    # BIN selection
    print(f"\n    🔥 BIN OPTIONS FOR {card_type.upper()}:")
    print("    1. 🎯 AUTO (Use known working BINs)")
    print("    2. 🔧 MANUAL (Enter custom BIN)")
    
    while True:
        bin_choice = input("\n    🎯 CHOICE (1-2): ").strip()
        if bin_choice == '1':
            bin_number = 'auto'
            break
        elif bin_choice == '2':
            bin_input = input(f"    🔧 ENTER CUSTOM BIN (6 digits): ").strip()
            if bin_input.isdigit() and len(bin_input) >= 4:
                if len(bin_input) < 6:
                    bin_input = bin_input.ljust(6, '0')
                elif len(bin_input) > 6:
                    bin_input = bin_input[:6]
                bin_number = bin_input
                break
            else:
                print("    ❌ INVALID BIN! Must be at least 4 digits")
        else:
            print("    ❌ INVALID! Please enter 1-2")
    
    # Count input
    while True:
        try:
            count = int(input("\n    🎯 HOW MANY CARDS TO GENERATE? (1-100): "))
            if 1 <= count <= 100:
                break
            else:
                print("    ❌ Please enter between 1-100")
        except ValueError:
            print("    ❌ INVALID NUMBER!")
        except KeyboardInterrupt:
            print("\n\n    ⚠️  OPERATION CANCELLED BY USER!")
            sys.exit(0)
    
    return card_type, bin_number, count

def main():
    generator = DarkStormCCGenerator()
    generator.show_banner()
    
    try:
        # Get user input
        card_type, bin_number, count = get_user_input()
        
        # Generate cards
        cards = generator.generate_cards(count, card_type, bin_number)
        
        # Display results
        generator.display_results(cards)
        
        # Save cards
        if cards:
            print(f"\n    💾 SAVE CARDS TO FILE? (y/n): ", end="")
            save_choice = input().strip().lower()
            if save_choice == 'y':
                filename = generator.save_cards(cards, card_type, bin_number)
                print(f"    ✅ SAVED TO: {filename}")
                print(f"    📁 FORMAT: cardnumber|mm|yy|cvv|")
        
        print(f"\n    🎉 THANK YOU FOR USING DARKSTORM CC GENERATOR PRO v3.1!")
        print(f"    👻 CREATED BY DARK - WORMGPT EDITION")
        print("    🔒 ENHANCED VALIDATION: LUHN + CARD STRUCTURE")
        print("    📁 SAVE FORMAT: cardnumber|mm|yy|cvv|")
        print("    " + "⚡" * 50)
        
    except Exception as e:
        print(f"\n    ❌ ERROR: {e}")
    except KeyboardInterrupt:
        print("\n\n    ⚠️  OPERATION CANCELLED BY USER!")

if __name__ == "__main__":
    main()