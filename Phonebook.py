# Phonebook 

#To store Names and numbers
Dhaman = {}
Qoyska = {}
Asxbt = {}
Shaqo = {}
Isku_fasal = {}

# function can display all numbers stored
def dhaman():
	print()
	print('Name\t\tNumbers')
	for key in Dhaman:
				print('{}\t\t{}'.format(key, Dhaman.get(key)))
	print()
# Loop to repeat commands
while True:
	print('-::::::Phonebook-::::::')
	print()
	print('Dooro qeybta aad rabto:')
	print('1.Dhammaan  \n2.Qoyska \n3.Asxaabta \n4.Shaqo_wadaag \n5.Isku fasal')
	print('《Guji 6 si aad u aragto numberada aad keydisay》')
	print('6.Soo bandhig dhammaan numberada keydsan')
	dor = input() # to choose options above
	#Dhammaan
	if dor == '1':
		print('《Dhammaan》')
		print()
		print('1.Keydi number \n2.Soo bandhig \n3.Raadi...* \n4 wax ka badal ku samey \n5.Tirtir number horey u jiray')
		choice = input()
		if choice == '1':
			print('KEYDI NUMBER:')
			Magac = input('Magaca: ')
			if Magac not in Dhaman:
				Num = input('Numberka: ')
				Dhaman[Magac] = Num
				print('')
				print("Numberka {} waa la keydiyey mahadsanid".format(Num))
				print()
			else:
				print("waanka xunnahay {} numberkiisa horay ayuu u jiray".format(Magac))
		elif choice == '2':
			print('Name\t\tNumbers')
			for key in Dhaman:
				print('{}\t\t{}'.format(key, Dhaman.get(key)))
		elif choice == '3':
			Raadi = input('Geli magaca qofka numberkisa aad raadineyso: ')
			if not Dhaman:
				print('Waxba lama keydin wali !')
			elif Raadi in Dhaman:
				print('{} : {}'.format(Raadi, Dhaman.get(Raadi)))
			else: 
				print("Lama helin {} numberkiisa/keeda".format(Raadi))
		elif choice == '4':
			badal = input('Geli magaca qofka numberkisa badalayso: ')
			if not Dhaman:
				print('Waxba lama keydin wali !')
			elif badal in Dhaman:
				en = input('Geli numberka cusub: ')
				Dhaman[badal] = en
				print('Howshaan waa lagu guulaystay mahadsanid')
				print('{} : {}'.format(badal, Dhaman.get(badal)))
		elif choice == '5':
			de = input('Geli numberka aad tirayso: ')
			if not Dhaman:
				print('Waxba lama keydin wali !')
			elif de in Dhaman :
				print('Mahubtaa inaad Tirtireyso {} numberkiisu yahay {} \n1.Haa \n2.Maya'.format(de, Dhaman.get(de)))
				hu = input()
				if hu == '1':
					Dhaman.pop(de)
					print("Howshaan waa lagu guulaystay!")
				else:
					print("Howshaan laguma guuleysan !")
	# Dhamaaan choose 1 ended
	#Qoyska started
	elif dor == '2':
				print('《Qoyska》')
				print()
				print('1.Keydi number \n2.Soo bandhig \n3.Raadi...* \n4 wax ka badal ku samey \n5.Tirtir number horey u jiray')
				choice = input()
				if choice == '1':
					print('KEYDI NUMBER:')
					Magac = input('Magaca: ')
					if Magac not in Qoyska:
						Num = input('Numberka: ')
						Qoyska[Magac] = Num
						Dhaman[Magac] = Num
						print('')
						print("Numberka {} waa la keydiyey mahadsanid".format(Num))
						print()
					else:
						print("waanka xunnahay {} numberkiisa horay ayuu u jiray".format(Magac))
				elif choice == '2':
					print('Name\t\tNumbers')
					for key in Qoyska:
						print('{}\t\t{}'.format(key, Qoyska.get(key)))
				elif choice == '3':
					Raadi = input('Geli magaca qofka numberkisa aad raadineyso: ')
					if not Qoyska:
						print('Waxba lama keydin wali !')
					elif Raadi in Qoyska:
						print('{} : {}'.format(Raadi, Qoyska.get(Raadi)))
					else:
						print("Lama helin {} numberkiisa/keeda".format(Raadi))
				elif choice == '4':
					badal = input('Geli magaca qofka numberkisa badalayso: ')
					if not Qoyska:
						print('Waxba lama keydin wali !')
					elif badal in Qoyska:
						en = input('Geli numberka cusub: ')
						Qoyska[badal] = en
						Dhaman[badal] = en
						print('Howshaan waa lagu guulaystay mahadsanid')
						print('{} : {}'.format(badal, Qoyska.get(badal)))
				elif choice == '5':
						de = input('Geli numberka aad tirayso: ')
						if not Qoyska:
							print('Waxba lama keydin wali !')
						elif de in Qoyska :
							print('Mahubtaa inaad Tirtireyso {} numberkiisu yahay {} \n1.Haa \n2.Maya'.format(de, Qoyska.get(de)))
							hu = input()
							if hu == '1':
								Dhaman.pop(de)
								Qoyska.pop(de)
								print("Howshaan waa lagu guulaystay!")
						else:
							print("Howshaan laguma guuleysan !")
	#Qoyska ended
	#Asxaabta starting 
	elif dor == '3':
				print('《Asxaabta》')
				print()
				print('1.Keydi number \n2.Soo bandhig \n3.Raadi...* \n4 wax ka badal ku samey \n5.Tirtir number horey u jiray')
				choice = input()
				if choice == '1':
					print('KEYDI NUMBER:')
					Magac = input('Magaca: ')
					if Magac not in Asxbt:
						Num = input('Numberka: ')
						Asxbt[Magac] = Num
						Dhaman[Magac] = Num
						print('')
						print("Numberka {} waa la keydiyey mahadsanid".format(Num))
						print()
					else:
						print("waanka xunnahay {} numberkiisa horay ayuu u jiray".format(Magac))
				elif choice == '2':
					print('Name\t\tNumbers')
					for key in Asxbt:
						print('{}\t\t{}'.format(key, Asxbt.get(key)))
				elif choice == '3':
					Raadi = input('Geli magaca qofka numberkisa aad raadineyso: ')
					if not Asxbt:
						print('Waxba lama keydin wali !')
					elif Raadi in Asxbt:
						print('{} : {}'.format(Raadi, Asxbt.get(Raadi)))
					else:
						print("Lama helin {} numberkiisa/keeda".format(Raadi))
				elif choice == '4':
					badal = input('Geli magaca qofka numberkisa badalayso: ')
					if not Asxbt:
						print('Waxba lama keydin wali !')
					elif badal in Asxbt:
						en = input('Geli numberka cusub: ')
						Asxbt[badal] = en
						Dhaman[badal] = en
						print('Howshaan waa lagu guulaystay mahadsanid')
						print('{} : {}'.format(badal, Asxbt.get(badal)))
				elif choice == '5':
						de = input('Geli numberka aad tirayso: ')
						if not Asxbt:
							print('Waxba lama keydin wali !')
						elif de in Asxbt :
							print('Mahubtaa inaad Tirtireyso {} numberkiisu yahay {} \n1.Haa \n2.Maya'.format(de, Asxbt.get(de)))
							hu = input()
							if hu == '1':
								Dhaman.pop(de)
								Asxbt.pop(de)
								print("Howshaan waa lagu guulaystay!")
						else:
							print("Howshaan laguma guuleysan !")
	#Asxaabta  ended
	#shaqo wadaag starting 
	elif dor == '4':
				print('《Shaqo-wadaag》')
				print()
				print('1.Keydi number \n2.Soo bandhig \n3.Raadi...* \n4 wax ka badal ku samey \n5.Tirtir number horey u jiray')
				choice = input()
				if choice == '1':
					print('KEYDI NUMBER:')
					Magac = input('Magaca: ')
					if Magac not in Shaqo:
						Num = input('Numberka: ')
						Shaqo[Magac] = Num
						Dhaman[Magac] = Num
						print('')
						print("Numberka {} waa la keydiyey mahadsanid".format(Num))
						print()
					else:
						print("waanka xunnahay {} numberkiisa horay ayuu u jiray".format(Magac))
				elif choice == '2':
					print('Name\t\tNumbers')
					for key in Shaqo:
						print('{}\t\t{}'.format(key, Shaqo.get(key)))
				elif choice == '3':
					Raadi = input('Geli magaca qofka numberkisa aad raadineyso: ')
					if not Shaqo:
						print('Waxba lama keydin wali !')
					elif Raadi in Shaqo:
						print('{} : {}'.format(Raadi, Shaqo.get(Raadi)))
					else:
						print("Lama helin {} numberkiisa/keeda".format(Raadi))
				elif choice == '4':
					badal = input('Geli magaca qofka numberkisa badalayso: ')
					if not Shaqo:
						print('Waxba lama keydin wali !')
					elif badal in Shaqo:
						en = input('Geli numberka cusub: ')
						Shaqo[badal] = en
						Dhaman[badal] = en
						print('Howshaan waa lagu guulaystay mahadsanid')
						print('{} : {}'.format(badal, Shaqo.get(badal)))
				elif choice == '5':
						de = input('Geli numberka aad tirayso: ')
						if not Shaqo:
							print('Waxba lama keydin wali !')
						elif de in Shaqo :
							print('Mahubtaa inaad Tirtireyso {} numberkiisu yahay {} \n1.Haa \n2.Maya'.format(de, Shaqo.get(de)))
							hu = input()
							if hu == '1':
								Dhaman.pop(de)
								Shaqo.pop(de)
								print("Howshaan waa lagu guulaystay!")
						else:
							print("Howshaan laguma guuleysan !")
	#shaqo wadaag   ended
	#iskufasal starting 
	elif dor == '5':
				print('《Isku-fasal (Classmates)》')
				print()
				print('1.Keydi number \n2.Soo bandhig \n3.Raadi...* \n4 wax ka badal ku samey \n5.Tirtir number horey u jiray')
				choice = input()
				if choice == '1':
					print('KEYDI NUMBER:')
					Magac = input('Magaca: ')
					if Magac not in Isku_fasal:
						Num = input('Numberka: ')
						Isku_fasal[Magac] = Num
						Dhaman[Magac] = Num
						print('')
						print("Numberka {} waa la keydiyey mahadsanid".format(Num))
						print()
					else:
						print("waanka xunnahay {} numberkiisa horay ayuu u jiray".format(Magac))
				elif choice == '2':
					print('Name\t\tNumbers')
					for key in Isku_fasal:
						print('{}\t\t{}'.format(key, Isku_fasal.get(key)))
				elif choice == '3':
					Raadi = input('Geli magaca qofka numberkisa aad raadineyso: ')
					if not Isku_fasal:
						print('Waxba lama keydin wali !')
					elif Raadi in Isku_fasal:
						print('{} : {}'.format(Raadi, Isku_fasal.get(Raadi)))
					else:
						print("Lama helin {} numberkiisa/keeda".format(Raadi))
				elif choice == '4':
					badal = input('Geli magaca qofka numberkisa badalayso: ')
					if not Isku_fasal:
						print('Waxba lama keydin wali !')
					elif badal in Isku_fasal:
						en = input('Geli numberka cusub: ')
						Isku_fasal[badal] = en
						Dhaman[badal] = en
						print('Howshaan waa lagu guulaystay mahadsanid')
						print('{} : {}'.format(badal, Isku_fasal.get(badal)))
				elif choice == '5':
						de = input('Geli numberka aad tirayso: ')
						if not Isku_fasal:
							print('Waxba lama keydin wali !')
						elif de in Isku_fasal :
							print('Mahubtaa inaad Tirtireyso {} numberkiisu yahay {} \n1.Haa \n2.Maya'.format(de, Isku_fasal.get(de)))
							hu = input()
							if hu == '1':
								Dhaman.pop(de)
								Isku_fasal.pop(de)
								print("Howshaan waa lagu guulaystay!")
						else:
							print("Howshaan laguma guuleysan !")
	#shaqo wadaag   ended
	
	
	#Display all the numbers
	elif dor == '6':
		dhaman()


# End 


# copyright of this code : Eng Abdirizak abdullahi hussein