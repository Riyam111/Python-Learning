import json
def load_data():
    try:
        with open('yotube.txt','r') as file:
          return   json.load(file)
    except FileNotFoundError:
          return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
   for index,videos in enumerate(videos,start=1):
       print(f"{index}.")
def add_video(videos):
    name=input("enter video name: ")
    time=input("enter video time: ")
    videos.append({'name': name,'time': time})
    save_data_helper(videos)


def update_video(video):
    pass
def delete_video(video):
    pass
def main():
    videos=load_data();
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List a favourite videos")
        print("2. add a youtube video")
        print("3. Update a youtube video")
        print("4. delete a youtube video")
        print("5. Exit the app")
        choice= input("Enter your choice")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")      
# Only run this part if the file is executed directly, not when imported.       
if __name__ =="__main__":
    main()        
