# **Hang Man**
### **Site Aims:**
​
Hangman in a terminal.
​
### **Color Scheme:**
​
We usually don't have much of a color scheme except White, Red, Blue and green. The exact hexagon codes I can sandly not provide considering I don't remember them fully myself at this point. 
​
## **Current Features Common to all pages**
​
## **Future-Enhancements**

* What can be made in the future is adding more letters into the two_word.py file. Potentially adding a third option which would give you three words instead of one or two, there can also be visual updates and improvement on the codes.
​
## **Testing Phase**

The testing phase was mostly trial and errors. I managed to run into a lot of issues considering I didn't know how to add a spacing between words which usually ended up with me not being able to figure to fit in the 2nd word section. That was helped by my mentor during our last meeting. Otherwise the testing phase was honestly writing out the code and testing. I figured also that my print sections was broken in an early stage as it didn't show the Hangman figure as it should but only showed if a letter was right or wrong. Figured out that was an issue with the print statement and solved it by removing the overlapping text.​

Tested the code through the [Python validator](https://pep8ci.herokuapp.com/) And everything came back clean. Of course the only issues was the remaining invalid escape sequences and the error line on 336 which is noted in bugs section.
​
​
## **Bugs**
​
* There is an issue of a lot of the lines complaining about 'invalid escape sequence '\ 'flake8(W605)
Anomalous backslash in string: '\ '. String constant might be missing an r prefix.pylint(anomalous-backslash-in-string)'
which is unable to be fixed. This is not an error just an complaining from Python however to make the good looking signs they need to be added there :P

* On line 336 there is a complaining section about a 'to long line' however that isn't sadly something that can be solved. Wherever I cut the line it complains in any sort of error and in the end the code is working and running fine.

On line 66 is an empty drawspace. That is currently needed as to not break the entire Logo section. If that line is removed the end sequence is activated and the entire line becomes distorted ruining the Hangman text.
​
***
## **Deployment**
I deployed the page on GitHub pages via the following procedure: -
​
1. From the project's [repository](https://github.com/Fisboll/Hangman), go to the **Settings** tab.
2. From the left-hand menu, select the **Pages** tab.
3. Under the **Source** section, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
​
You  can find the live site via the following URL - [live webpage](https://yoururlhere)
***
​
## **Tech**
​
Here mention what technologies you've used for example
​
-Python
​
## **Credits**
### **Honorable mentions**

[Took the class of colors](https://github.com/gibbo101/hangman/blob/main/run.py)
This one I took the hangman pictures, Of course. I also took the base of how they made their difficult levels. [Where I got most inspiration](https://github.com/Bethieieio/project-three-console-hangman)

And my last mention is of course my amazing Mentor who helped me through it all!
​
It's always nice to mention those that helped you get there, if people gave you support on slack or the local cat scared you into completing give them a mention!
​
### **Content:**
​
If you took any code from online source and by this i mean copy paste with zero changes mention it here!