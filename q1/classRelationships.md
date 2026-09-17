# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Song_stats
Description: A class that shows selected stats about a song, like its singer

## New Related Class
Class: Artist
Description: A class that compiles all the authors songs and does some more things

## Association
Relationship: Artist ----owns---- Song
Explanation:  An song artist owns the song they made.

## Multiplicity
Multiplicity: one to many
Explanation: An artist can own many, many songs.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association between my classes is that an author creates many songs in an entire career. They are associated with the Songs being created by the author.

### What multiplicity did you choose and why?
I chose 1 to many, since one author/artist can have as many songs as he wants. 

### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
Storing an object reference is significantly easier than just copying its data. You won't have to type more code and you could be more efficient

### If your relationship uses many, why is a list appropriate?