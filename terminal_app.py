
import httpie

def main():
        print("\n\t*** Python HTTP API Terminal App ***\n\t\n")
        print("Hey, welcome to this simple Python HTTP API command line app")
        print("Let's post a cool comment on an issue on Github!")


        
        
        
        print("\nNow let's add a new comment...")

        default_comment = "Just say TIA. This Is Andela! :heart: "
        user_comment = input("We have a nice default comment for you, press enter to post it. But if you want your, just input it here: ")

        print("\n\tReady to post it?\n")
        username = input("Now enter your Github username: ")

        username = input("Now enter your Github username: ")
        if user_comment == "":
	        http -a username POST https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments body=default_comment
        else:
	        http -a username POST https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments body=user_comment + ' :heart:'
	
	print("\n\t Posting your cool comment...\n")
	
if __name__ == '__main__':
	main()