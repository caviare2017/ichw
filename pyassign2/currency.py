#!/usr/bin/env python3

"""currency_exchange.py: currency_exchange is a procedure used for exchanging
a certain amount of currency_A to currency_B.You should key in the relating in-
formation in such a format:"from=source&to=target&amt=amount"
   in this expression, source is the type of currency you have
                       target is the type of currency you want to exchange to
                       amount is how much you want to exchange.
   We also give a primary test procedure,in which we can have a basic examination
of the main function.
__author__ = "Yang Zhengji"
__pkuid__  = "1700011817"
__email__  = "1700011817@pku.edu.cn"
"""


def test_All():
    """Module test_All is written for testing the whole procedure.And in this
    module, it contains 4 parts of tests and every test module under it,there
    are also hints that show if it passes successfully"""
    def test_exchange_convert():
        """This procedure is to test "exchange_convert",which is used for converting the
        input strings to a tuple.And so we can invoke data in it easily.
        Return: pass message"""
        
        print("***Unit test for module exchange_convert (First part).***")
        get_from=exchange_convert("from=USD&to=EUR&amt=2.5")
        target=["USD","EUR",2.5]
        for i in range (3):
            assert(get_from[i] == target[i])

        print("***Module exchange_convert (First part) passed test_1.***")


    def test_get_from_and_to():
        """This test-procedure is written for testing the "get_from_and_to"
        Return: pass message"""
        
        print("***Unit test for module get_from_and_to (Second part).***")
        get_from=get_from_and_to('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}')
        target=["2 United States Dollars","1.825936 Euros"]
        for i in range (2):
            assert(get_from[i] == target[i])

        print("***Module get_from_and_to (Second part) passed test_2.***")

    def test_currency_response():
        """Test for currency_response.
        Return: pass message"""
        
        print("***Unit test for module currency_response (Third part).***")
        get_from=currency_response("USD","EUR",2.5)
        target='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
        assert(get_from == target)

        print("***Module currency_response (Third part) passed test_3.***")
        return



    def test_exchange_main():
        """As the final-part-test,this procedure not only examine the error in PartⅣ
        but also helps in improving the connections between each part.
        Return: pass message"""

        
        print("***Unit test for module exchange_main (Final part).***")
        get_from=exchange_main("from=USD&to=EUR&amt=2.5")
        target=float(2.0952375)
        assert(get_from == target)

        print("***Module exchange_main (Final part) passed test_4.***")
        return

    print("***test all cases***")
    test_exchange_convert()
    test_get_from_and_to()
    test_currency_response()
    test_exchange_main()
    print("All tests passed")

def exchange_convert(exchange_str):
    """The format of input is "from=source&to=target&amt=amount"
    parameter:the string to slice
    returns:2 Substrings and a float."""
        
    exchange_list=exchange_str.split("=")
    exchange_to=[]
    for i in range(len(exchange_list)):
        exchange_to +=(str(exchange_list[i]).split("&"))
    currency_from=exchange_to[1]
    currency_to=exchange_to[3]
    amount_from=float(exchange_to[5])
    return (currency_from,currency_to,amount_from)


def currency_response(currency_from,currency_to,amount_from):
    """In this procedure ,data input will make a call to the target webset,and a string
    containing relating information will be put out.
    parameter:currency_from(str);currency_to(str):amount_from(float)
    return:a string from the target webset"""
     
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def get_from_and_to(data_feedback):
    """This procedure is used for fetching the information recieved from the target
    webset,and transform it into a tuple.
    parameter:the string from the webset
    return:a tuple including amount_from,currency_from and amount_to,currency_to"""
    
        
    if "false" in data_feedback:
        print("Error,the format of data input is wrong")
        return exit(1)
    else:
        data_feedback=str(data_feedback).split("\"")
        list_get=[]
        for i in range(len(data_feedback)):
            if (data_feedback[i]+" ")[0].isdigit():
                list_get.append(data_feedback[i])
        tuple_get=tuple(list_get)
        return tuple_get
def exchange_main(currency):
    """In this module, the modules we write is integrated together.And the final
    result is given.
    parameter:string with the format of "from=source&to=target&amt=amount"
    return:a float of the amount exchangeg to"""
    
    currency_from=exchange_convert(currency)[0]
    currency_to=exchange_convert(currency)[1]
    amount_from=exchange_convert(currency)[2]
    exchange_feedback=currency_response(currency_from,currency_to,amount_from)
    amount_to_str=get_from_and_to(exchange_feedback)[1].split(" ")[0]
    amount_to=float(amount_to_str)
    return amount_to
def main():
    print("***The format of your input should be:from=source&to=target&amt=amount***")
    print(""""Attention:""")
    print("'source'、'target'should be a valid string including 3 capital letters")
    print("""'amt'should be a float or int" """)
    print("Please key in the currency string:")
    currency_ex=input()  
    if "from=" in currency_ex and "to=" in currency_ex and "amt=" in currency_ex:
        print(exchange_main(currency_ex))

    else:
        print("The format is wrong!!!")
        print("If you want to run this procedure again,key in 'Y' in represent for 'Yes'")
        judge_1=input()
        if judge_1 =="Y":
            main()
        else:
            pass

    print("If you want to test the procedure,key in 'Y' in represent for 'Yes'")
    judge_2=input()
    if judge_2 == "Y":
        test_All()
    else:
        return
    input()

    
if __name__ == '__main__':
    main()
    
