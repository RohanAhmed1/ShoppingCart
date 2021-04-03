#Main Program starts from here.
from CustomerDB import CustomerDB
from ProductDB import ProductDB
from Cart import Cart
        
print(' ______________________________________________________________________________________________________________________________________________   ')
print('|*                                                                                                                                             |  ')
print('| **                ****  **    * *    ***** **    * ****      **** *   *  ****  **** **** ***** **    * *****      *****  ****  **** *****    |  ')
print('|  ***             *    * * *   * *      *   * *   * *         *    *   * *    * *  * *  *   *   * *   * *          *     *    * *  *   *      |  ')
print('|   *************  *    * *  *  * *      *   *  *  * *         **** *   * *    * **** ****   *   *  *  * *          *     *    * ****   *      |  ')
print('|    ***********   *    * *   * * *      *   *   * * ****         * ***** *    * *    *      *   *   * * * ***      *     ****** **     *      |  ')
print('|     *********    *    * *    ** *      *   *    ** *            * *   * *    * *    *      *   *    ** *   *      *     *    * * *    *      |  ')
print('|     **     **     ****  *     * **** ***** *     * ****      **** *   *  ****  *    *    ***** *     * *****      ***** *    * *  *   *      |  ')
print('|______________________________________________________________________________________________________________________________________________|  ')
print('|    Welcome       In         Our        Online        Store.     We       have        Unique      and        Original          Products       |  ')
print('|______________________________________________________________________________________________________________________________________________|  ')

while True:
    print('\n====================================\n')
    print('\t1. Sign up\n\t2. Sign in\n\t3. Exit')
    print('\n====================================')
    print('***Intructions***')
    print("If you are New in our Online Store, Press '1' for 'Sign up', if you already have ID in our Store, Press '2' for 'Sign in'\
 ,and Press '3' for 'Exit'.\n")
    ans1=input('Enter your Choice:')
    print()
    CDB=CustomerDB()
    if ans1=='1':
        CDB.addCustomer()
        CDB.saveCustomerList()
        print('\nYou Signed up Succesfully.\n')
    elif ans1=='2':
        while True:
            print()
            user_id=input('Enter the ID:')
            user_pass=input('Enter the Password:')
            #check the customer data in file
            if CDB.checkid(user_id,CDB.CustomerList) and CDB.checkpassword(user_pass,CDB.CustomerList):
                PDB=ProductDB()
                PDB.printProductList()
                C=Cart()
                print('\n=============================================\n')
                print('\tReady to Select Your Product')
                print('\t1. Add the Product into your Cart')
                print('\t2. Remove the Product from your Cart')
                print('\t3. Show your Cart')
                print('\t4. Checkout')
                print('\t5. Show Shopping Hsistory')
                print('\t6. Exit')
                print('\n=============================================\n')
                print('***Intructions***')
                print("Press '1' for 'Add the Product into your Cart', Press '2' for 'Remove the Product from your Cart', Press '3' for 'Show your Cart'")
                print("Press '4' for 'Checkout', Press '5' for 'Shopping Hsistory' and Press '6' for 'Exit'")
                while True:
                    print()
                    ans2=input('Enter your Choice:')
                    print()
                    if ans2=='1':
                        C.addselectedProduct()
                    elif ans2=='2':
                        C.removeselectedProduct()
                    elif ans2=='3':
                        C.printCart()
                    elif ans2=='4':
                        C.checkout()
                    elif ans2=='5':
                        C.CustomerShoppingHistory()
                    elif ans2=='6':
                        break
                    else:
                        print('\nEnter your Choice according to the given Instruction.\n')
                break
            else:
                print('\nYou Enter, either wrong ID or Password, or you don\'nt have ID and If you don\'nt have ID, please Sign up first.\n')
                break
    elif ans1=='3':
        break
    else:
        print('\nEnter your Choice according to the given Instructions.\n')


#Ending of the Program
print('\nThanks for visiting,Sir. We hope, you like our Product and visit again.')
print('Good Bye and Take Care.')
