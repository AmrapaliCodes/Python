# You got the transcript for a chat conversation in a dictionary format.
# ex.
# {1: “my phonenumber is 9012912012”,
# 2: "my email id is xyz.com and my phone no is 9012912041 "}
# Create a list considering the below details:
# 1. List should have only the phone numbers
# 2. Skip all the invalid phone number ( numbers > 10 digit)
# 3. Append the country code +91 in from of the phone number before adding to the list.


def phone_list(msg):
# 1st Approach: Naive
    list=[]
    phone_list=[]
    for i in msg:
        list.extend(msg[i].split())

    for i in list:
        if i.isdigit():
            if len(i)<=10:
                phone_list.append("+91"+i)
    print(phone_list)

# 2nd Approach: Short
    phone_list = ['+91' + word for line in msg.values() for word in line.split() if word.isdigit() and len(word)<=10]
    print(phone_list)

msg={
    1: "my phonenumber is 9012912012",
    2: "my email id is xyz.com and my phone no is 9012912041 ",
    3: "hey there 321345532",
    4: "890076"
    }

phone_list(msg)