# ENCOMP

 - WHAT IS ENCOMP

** ENCOMP ** is a dictionary compression method, developed on ** Python ** language.
It is ranked as the best on the internet, given comparisons with the two most popular compression methods: ** 7z ** and ** Winzip **.
***
 - HOW DOES IT WORK

It uses a list of ** 279.894 ** Italian words, ordered in order of increasing length, called "* dictionary *", to compress sentences or words of any length, syntactically correct or not.

The program will make them incomprehensible to those who do not have the "dictionary", making this compression method also an efficient coding method.
***
 - PSEUDOCODIFICATION
> Suppose we had to compress and encode the word
> "Comparative".
> We insert the word "comparati" into the Python script.
> The program will search for the same word in the "dictionary" and
> will report its position in the word list.
>
>. . .
>
> 91,210 compared
>
> 91,211 compared
>
> 91,212 compared <<<
>
> 91,213 compared
>
> 91,214 will appear
>
>. . .
>
> The word “comparati” is located in position 91.212.
>
> We can see how, using only this first conversion,
> this method was able to save 4 characters. ("Compare" >>>
> "91212")
>
> The program then converts this number from decimal to hexadecimal.
>
> ("91212" >>> "1644c")
>
> In this case the number of characters has not been reduced but if the
> position had been “12389”, converted into hexadecimal, it would result
> same as “3065”, saving additional characters.
>
> The accents of the inserted string will be removed.
>
> The punctuation of the entered string will be removed.
>
> Uppercase letters will be changed to lowercase.
>
> If the inserted string contains numbers, we will proceed
> converting the number to hexadecimal, adding an exclamation point
> "!" after the last digit.
>
> ("2021" >>> "7e5!")
>
> The number will not be compressed.
>
> Words with grammatical errors or those that do not exist within the
> list will be reported as original.
>
> ("Compartai" >> "compartai")

***
 - LIMITS

** ENCOMP ** currently only supports the Italian language, but it is not excluded that other languages ​​may be added in the future.

This compression method is based on a dictionary, therefore the accents of the inserted string will be removed, the punctuation of the inserted string will be removed, the uppercase letters will be changed to lowercase. In the future this may change and for this very reason, currently, it is a lossy compression.
***

 - BENEFITS

One of the most advantageous aspects of ** ENCOMP ** is to leave the compressed file in a file with ".txt" format, avoiding extension changes that could cause the file size to increase.

The comparisons between ** 7zip, WinZip and ENCOMP ** are shown below.
! [comparison] (https://user-images.githubusercontent.com/91328373/147512599-0fea471c-8c50-4679-8c11-d7643441aa2d.png)


Original file: 381 bytes
7z: 391 bytes
WinZip: 351 bytes
ENCOMP: 248 bytes

Compression ** ENCOMP **, out of the 3, * is the best *.



** The content of the original file is **: "

> It uses a list of 279,894 Italian words, sorted in order
> increasing in length, called "dictionary", to compress sentences or
> words of any length, syntactically correct or not. The
> program will make them incomprehensible to the eyes of those who do not have the right
> possess the "dictionary", making this compression method too
> an efficient coding method.

"

** The content of the file compressed with the ENCOMP method is **: "

> 32a a209 111 1360 c 44556! 3f7b ef10 ff13 1a 3e14 167ae c 19189 d9b
> "dictionary" e2 215ca 1017 4 3f7b c 1afc9 19189 42ed8 d340 2 cc 19
> 1adbe 1e 977f 424ab 145 164c c 6e cc 17 1a 10887 19 "dictionary" 10f6c
> 42aa 3a96 c 354c9 83d 32 22307 3a96 c d058

"

** The content of the unzipped file is **: "

> it uses a list of 279894 Italian words sorted in order
> increasing length called "dictionary" to compress phrases or
> words of any length syntactically correct and not the
> program will make them incomprehensible to those who do not have the right
> possess the "dictionary" by making this compression method also
> an efficient coding method

"

In the future ** ENCOMP ** will be improved, also integrating punctuation, capital letters and accents.
