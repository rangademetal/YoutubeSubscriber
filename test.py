from subscribe.youtube import Youtube

youtube = Youtube("YOUR USERNAME", "YOUR PASSWORD")
youtube.loginYoutube()
arr = [
    'https://www.youtube.com/channel/UCqP3EFpcxWlR_Ne8ImA533w/',
    'https://www.youtube.com/channel/UCn78EWOxiDLast6U6e-Z_fA'
]
youtube.giveSubscribe(arr)