# SG4 - Understanding Classes and Objects 
## Playlist
## My class represents a collection of tracks/songs that include details like track length, and title
## Properties 
| Property | Data Type | Description | 
|---|---|---| 
| Title | string | The song's title | 
| Singer | string | The person that sang the song | 
| Song_code | int | A one time code that brings you to the exact song and time| 
| Producer | string | The song's producer | 
## Methods 
| Method | Description | 
|---|---|
| add_song(Song_Title:string) | Adds a song with the same song title | 
| play() | Plays the song that is next or the song thats paused | 
| delete_song(Song_Title:string) | Deletes the selected song if found in the playlist | 
## Class Diagram 
[Class_Diagram](q1/images/Screenshot2026-09-03125917.png)
## Design Explanation 
### Why did you choose this class? 
I chose this class since I like playing music in my earpods during free time. It also somewhat helps me concentrate.

### Which property is the most important? Why? 
The property that is the most important  is the title, since the user can find songs witha  title but it will be extremely hard without a title.

### Which method is the most useful? Why? 
Play song, you can play a song without needing to add it or delete it first, therefore I will be able to play songs even when not logged in 

## Design Revision
Changes from my previous design:
- replace Duration with Song_code

| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Title | string | Public | Public since a title contains data that is needed for a user to find it|
| Singer | string | Public | Public since a Singer relies on the released songs for their fanbase and the singers can also be used to search for the songs| 
|  Song_code | int | Private | Private since this is a one time link that can be used to either share or receive songs |
| Producer | string | Public | Public since producers are also a good way to search songs |

