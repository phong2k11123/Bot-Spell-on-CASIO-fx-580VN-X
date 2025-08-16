import time
import sys
import re
import string

def typewriter(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_menu():
    typewriter("\n===== Hack Casio =====", 0.07)
    time.sleep(0.5)
    typewriter("Tool Spell 1 line trên CASIO fx-580VN X", 0.05)
    typewriter("- Bản quyền © Hack Casio -", 0.05)
    typewriter("1. Lưu ý", 0.05)
    typewriter("2. Liên hệ", 0.05)
    typewriter("3. Spell", 0.05)

def show_notes():
    typewriter("\n===== Lưu ý sử dụng! =====", 0.05)
    notes = [
        "1. Khi spell chỉ được spell tối đa 17 kí tự nếu nhiều hơn sẽ không spell được!",
        "2. Không được phụ thuộc vào bot!",
        "3. Tool này hoàn toàn miễn phí không được bán bot để kiếm lời!",
        "4. Tôn trọng bot và người tạo ra tool!",
        "5. Không được sao chép tool dưới mọi hình thức!",
        "6. Tool đôi khi sẽ bị lỗi vui lòng cân nhắc trước khi sử dụng!",
        "7. Tool chỉ dành cho CASIO fx-580VN X các loại máy khác sẽ không làm được!",
        "8. Không được sửa tên người tạo ra Tool!",
        "9. Nếu trong quá trình sử dụng tool bị lỗi chổ nào vui lòng liên hệ để được hỗ trợ!"
    ]
    for note in notes:
        typewriter(f"  • {note}", 0.04)
        #time.sleep(0.8)

def show_contacts():
    typewriter("\n===== Liên hệ! =====", 0.04)
    contacts = [
        "Coder Feature: Phong2k11®",
        "Discord: Phong2k11®",
        "TikTok: Phong2k11®",
        "YouTube: Phong2k11",
        "Coder Tool Spell: AxesMC",
        "Discord: C++ My Life(@kiet130218_80627) or Kiet1302181(@kiet1302181)",
        "Tiktok: AxesMC or @typedcello07585",
        "Youtube: AxesMC"
    ]
    for info in contacts:
        typewriter(f"  • {info}", 0.04)
        #time.sleep(0.8)
#Cái def fill_template() này dùng để lấp hex vào biến A B C
def fill(hex_list):
	A=["1.0000","__", "__", "_!", "!_","__", "×10", "!!"]
	B=["1.", "__","__", "__", "_!", "!_","__", "×10", "!!"]
	C=["1.", "__","__", "__", "_!", "!_","__", "×10", "!!"]
	pos=0 #vi tri cua hex_list
	pos1=0 #vi tri slot cua cac variable A B C
	filled=[]
	id=0
	hex_list_edited = []
	pos3 = 0
	filled.append(" x:\n")
	#Xoa dau cach giua 2 bytes
	for phantu in hex_list:
		if len(phantu) == 5:
			xoa = phantu.replace(" ", "")
			hex_list[pos3] = xoa
		pos3+=1
	#Tach 2 bytes
	for phantu in hex_list:
		pos2 = 0
		while pos2 <= len(phantu):
			byte_edited = phantu[pos2:pos2+2]
			#Loc cac dau '' thua trong hex_list
			if byte_edited == '':
				break
			else:
				hex_list_edited.append(byte_edited)
			pos2+=2
	hex_list = hex_list_edited
	if len(hex_list)>20:
			return filled, 0, False
			
	'''
	ID = 0 thi chi bien A
	ID = 1 thi chi bien B
	ID = 2 thi chi bien C
	'''
	#Tach cac bien 2 bytes
	
	for i in range(100):
		if id==0:
			slot=A[pos1]
		elif id==1:
			slot=B[pos1]
		elif id==2:
			slot=C[pos1]
			
		if slot in ["1.0000", "1."]:
			if id==0:
				filled.append("A = ")
			if id==1:
				filled.append("B = ")
			if id==2:
				filled.append("C = ")			
			filled.append(slot)
			pos1+=1		
		if slot =="×10":
			filled.append(slot)
			pos1+=1
			
		else:
			byte=hex_list[pos]
			
			if slot=="__":
				filled.append(byte)
				pos+=1
				pos1+=1
				
			elif slot=="_!":
				if byte[1].isalpha():
					filled.append("20")
				else:
					filled.append(byte)
					pos+=1
				pos1+=1
				
			elif slot=="!_":
				if byte[0].isalpha():
					filled.append("20")
				else:
					filled.append(byte)
					pos+=1
				pos1+=1
				
			elif slot=="!!":
				if byte.isdigit():
					filled.append(byte)
					filled.append("\n")
					pos+=1
				elif byte[0].isalpha or byte[1].isalpha:
					if hex_list[pos-1] == "F4":
						filled.remove(hex_list[pos-1])
						filled.insert(pos-1, "20")
						pos-=1
						filled.append("20")
					else:
						filled.append("20")
					filled.append("\n")
				pos1=0
				id+=1 #id nay chi bien A B C
		if len(hex_list)==pos:
			break
	if len(filled)-6>20:
		return filled, id, False
	else:
		return filled, id, True
def spell_input():
    typewriter("Nhập câu bạn muốn spell trên CASIO fx-580VN X: ", 0.04)
    time.sleep(0.04)
    cau = input()
    while len(cau) > 17:
        typewriter("Câu nhập quá 17 kí tự ! Vui lòng nhập lại: ",0.04)
        cau = input()
        #time.sleep(0.8)
    ds_chu = list(cau)
    spaces = 17 - len(cau)
    # Căn lề giữa cho câu:
    if spaces % 2 == 0:
        spaces_lr = spaces // 2
        ds_chu = [' ' for i in range(spaces_lr)] + ds_chu + [' ' for i in range(spaces_lr)]
    # Căn lề lệch 1 dấu cách (do dư 1 dấu cách)
    elif spaces % 2 == 1:
        space_l = (spaces-1)//2
        space_r = space_l + 1
        ds_chu = [" " for i in range(space_l)] + ds_chu + [" " for i in range(space_r)]
    #Lọc kí tự ghi bằng Hex và kí tự ghi bằng phím
    count = 0
    chars_hex = ['a','b','c','d','e','f','g','j','k','L','M','N','O','T','U','V','W','X','Y','Z']
    hex_list = [] #Danh sách lưu các hex của các chữ không ghi bằng phím, lấy bằng hex
    chars_by_hex = [] #Các kí tự lấy bằng hex trong câu nhập vào
    chars_by_key = [] #Các kí tự lấy bằng key trong câu nhập vào
    hex_chars = [] #Kí tự hex, là chữ cái A B C D E F in đậm
    found_keys = {} #Phím
    found_hex_chars = {}
    all_ascii_chars = list(string.ascii_letters)
    for ki_tu in ds_chu: #Lọc
        if ki_tu in chars_hex: #Nếu kí tự nằm trong kí tự lấy bằng Hex
            chars_by_hex.append(ki_tu)
        elif ki_tu not in chars_hex and ki_tu in all_ascii_chars: #Nếu kí tự không nằm trong chars_hex, kí tự trong ascii và kí tự = dấu cách
            chars_by_key.append(ki_tu)
        elif ki_tu not in chars_hex and ki_tu not in all_ascii_chars and ki_tu!=" ": #Không nằm trong chars_hex, ko nằm trong ascii, khác dấu cách
            if ki_tu!="!":    
                chars_by_hex.append(ki_tu)
        elif ki_tu == "!":
            chars_by_key.append(ki_tu)
        elif ki_tu.isdigit():
             chars_by_key.append(ki_tu)
    # Lấy kí tự trong file
    with open("chars.txt", "r", encoding="utf-8") as file:
        lines = file.readlines() #Đọc file
        # Lấy kí tự lấy bằng hex
        for char in chars_by_hex:
            found = False
            for line in lines:
                line = line.strip()
                parts = line.split(" : ")
                if len(parts) >= 2 and parts[1] == char:
                    hex_code = parts[0]
                    if not char.isdigit():
                        typewriter(f"Hex của kí tự {char} là {hex_code}")
                        hex_list.append(hex_code)
                    else:
                        pass
                    found = True
                    break
            if not found:
                typewriter(f"Không tìm thấy kí tự {char} trong chars.txt !")

        # Lấy kí tự lấy bằng phím
        for line in lines:
            line = line.strip()
            if " : " in line:
                parts = line.split(" : ")
                if len(parts) == 3:
                    hex_code, char, button = parts
                    if char in ds_chu:
                        found_keys[char] = button
            if not found:
                typewriter(f"Không thể tìm thấy phím của kí tự {char} trong chars.txt")
    for byte in hex_list:
        for ki_tu_hex in byte:
            if ki_tu_hex in ["A", "B", "C", "D", "E", "F"]:
                hex_chars.append(ki_tu_hex)
    hex_chars.append("C")
    hex_list.append("3C")
    hex_list.append("23")
    with open("takechars.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        found = False
        for line in lines:
            line = line.strip()
            parts = line.split(" : ")
            for char in hex_chars:
                if len(parts) == 2:
                    if parts[0] == char:
                        key = parts[1]
                        found_hex_chars[char] = key
                        found = True
                        break
    list_lo=[] #Danh sách
    filled, id, status = fill(hex_list)
    if not status:
        typewriter("Số kí tự quá nhiều bytes, vui lòng nhập câu khác !", 0.04)
    for i in filled:
        list_lo.append(i)
    #Lấp hex_list vào A, B, C
    typewriter("Bước 1: Reset máy: \n [shift] [9] [3] [=] [=]", 0.03)
    #time.sleep(0.8)
    typewriter("Bước 2: Vào LineI/O: \n [shift] [menu] [1] [3]")
    #time.sleep(0.8)
    typewriter("Bước 3: Vào Basic Overflow: \n [x] [alpha] [CALC] [shift] [x] [x] [shift] [)] [9] [shift] [)] [9] [9] [9] [CALC] {[=] [AC]}-> nhấn nhanh [<] [del] [del] [CALC] [=] [<] [shift] [.]",0.04)
    #time.sleep(0.8)
    typewriter("Bước 4: Lấy kí tự Hex cần thiết: ",0.02)
    #time.sleep(0.8)
    for ki_tu_hex in hex_chars:
        print(found_hex_chars[ki_tu_hex])
        count+=1
    typewriter(f"Nhấn ([<] [9] [DEL])×{count}")
    typewriter("Bước 5: Làm như sau: ", 0.03)
    count=0 #Reset biến count để đếm lần 
    for i in list_lo:
        if i == "A = ":
            list_lo.remove(i)
        if i == "B = ":
            list_lo.remove(i)
        if i == "C = ":
            list_lo.remove(i)
    for byte in list_lo:
        if byte == "1.0000":
            print("[alpha] [(-)] [alpha] [CALC]", end=" ")
        elif byte == "1.":
            if count == 0:
                print("\n[alpha] [∫] [alpha] [□ ' \"]", end=" ")
                count+=1 #Tăng ID để chạy biến C= ở dưới
            elif count == 1:
                print("\n[alpha] [∫] [alpha] [x⁻¹]", end=" ")
        elif byte == 'x:':
            print("[x] [alpha] [∫]")
        elif byte == " ":
            pass
        else:
            for ki_tu in byte:
                if ki_tu.isdigit():
                    print(f"[{ki_tu}]", end=" ")
                elif ki_tu in ["A", "B", "C", "D", "E", "F"]:
                    print("[>]", end=" ")
                elif ki_tu == ".":
                    print("[.]", end=" ")
                elif byte=="×10":
                    print("[×10]", end=" ")
                    break
    typewriter("\nNó hiển thị như này là đúng nè:", 0.02)
    #time.sleep(0.8)
    print(' '.join(filled))
    typewriter('Bước 6: Lấy "an":\n[x] [alpha] [CALC] [shift] [x] [x] [shift] [)] [9] [shift] [)] [9] [CALC] [=] [<] [shift] [.] [shift] [.] [<] [<] [DEL] [v] [shift] [8] [v] [2] [6] [<] [<] [>] [9] [DEL] [<] [)] [+] [100 số bất kì]\n[CALC] [=]',0.04)
    #time.sleep(0.8)
    typewriter('Bước 7: Lấy "@":\n[x] [alpha] [CALC] [shift] [x] [x] [shift] [)] [9] [shift] [)] [9] [CALC] [=] [<] [shift] [.]',0.02)
    #time.sleep(0.8)
    if id == 0:
        typewriter('[shift] [7] [4] [8]', 0.03)
        typewriter('([<] [9] [DEL])×1\n[DEL]×10',0.02)
        typewriter('[<] [9 số bất kì] [>] [alpha] [∫] [>] [alpha] [CALC] [alpha] [(-)]\n[CALC] ([=])×2 [^]', 0.04)
    elif id == 1:
        typewriter('[shift] [7] [4] [8] [shift] [7] [4] [9]', 0.02)
        typewriter('([<] [9] [DEL])×2\n[DEL]×10', 0.02)
        typewriter('[<] [9 số bất kì] [>] [alpha] [∫] [>] [alpha] [CALC] [alpha] [(-)] [alpha] [∫] [>] [alpha] [CALC] [alpha] [□ \' "]\n[CALC] ([=])×3 [^]', 0.04)
    elif id == 2:
        typewriter('[shift] [7] [4] [8] [shift] [7] [4] [9] [shift] [7] [1] [4]', 0.04)
        typewriter('([<] [9] [DEL])×3\n[DEL]×10', 0.03)
        typewriter('[<] [9 số bất kì] [>] [alpha] [∫] [>] [alpha] [CALC] [alpha] [(-)] [alpha] [∫] [>] [alpha] [CALC] [alpha] [□ \' "] [alpha] [∫] [>] [alpha] [CALC] [alpha] [x^-1]\n[CALC] ([=])×4 [^]', 0.04)
    typewriter('Bước 8: Xóa bytes thừa:', 0.02)
    list_lo.reverse()
    if " x:\n" in list_lo:
        list_lo.remove(" x:\n")
    if "\n" in list_lo:
        list_lo.remove("\n")
    count=0
    for i in list_lo:
        if i=='20':
            if count==0:
                print("[DEL]",end=" ")
            else:
                print(f"[<]x{count} [DEL]",end=" ")
            count=0
        elif i=='1.':
            if count==0:
                print("[DEL]x2",end=" ")
            else:
                print(f"[<]x{count} [DEL]x2",end=" ")
            count=0
        elif i=='1.0000':
            if count==0:
                pass
            else:
                print(f"[<]x{count}",end=" ")
            count=0
        elif i == '×10':
            pass
        elif i == "F4":
            pass
        else:
            count+=1
    typewriter("\nBước 9: Gán chữ: ")
    b=0 # Biến đếm khi có kí tự 2 bytes
    for char in ds_chu:
        if char in found_keys:
            typewriter(found_keys[char],0.04)
            if char == " ":
                b+=1
        elif char not in found_keys:
            if char not in all_ascii_chars:
                typewriter("[>]", 0.04)
                time.sleep(0.8)
                b+=1 #Do không nằm trong kí tự Tiếng Anh và các kí tự ascii
            elif char in all_ascii_chars:
                if char in chars_by_hex:
                    typewriter("[>]",0.04)
                    time.sleep(0.8)
    typewriter(f"[{17-b} số bất kì] [shift] [(] [2] [x], việc còn lại là bấm [calc] [=]")
    typewriter(f"-----HẾT-----")
    typewriter("Coder Feature: Phong2k11®", 0.04)
    typewriter("Coder Tool Spell: AxesMC", 0.04)
def main():
    show_menu() #Hiện menu
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            show_notes()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            spell_input()
        else:
            typewriter("Lựa chọn không hợp lệ, vui lòng thử lại...", 0.04)

if __name__ == "__main__":
    main()


