def convert(str):
    output = str.replace(":)","🙂")
    final_output = output.replace(":(","🙁")
    return final_output

def main():
    str = input("Enter string: ")
    ans=convert(str)
    print(ans)

main()