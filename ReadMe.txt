SNS Project


||Part 1: Implemenatation of ReDos attack on the regex engine constructed from scratch and the fix to the vulnerability||

We constructed regex engine from scratch. We tried diffeent regular expressions and found an expression which is vulnerable to ReDos attack.The expression is A(B|C+)+D.

||OS used||: Ubuntu Linux 20.4 Lts

||Installations required||: flask

The following steps can be followed to run the application and perform the ReDoS atack:

Step 1: Install dependencies:

		pip3 install flask

Step 2: From a terminal open the location of the project: regex_from_scratch and run the following command:

	 python3 NonMemoapp.py

Step 3: In the Form UI, Enter a large input. (Eg: ABCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD)

This should make the application to keep on running showing that it is vulnerable to the ReDoS Attack.


|| Solution using a rectified version of the package ||

We used memoization approach to solve this problem. Instead of backtracking again and going to the same state multiple times, we stored the states of the input along with the regex. Beacuse of this recursive calls decreased and code became faster causing it less prone to ReDos attack.


The following steps can be followed to run the application with the fixed vulnerable code:

Step 1: From a terminal open the location of the project: regex_from_scratch and run the following command:

	 python3 Memoapp.py

Step 2: In the Form UI, Enter a large input. (Eg: ABCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD)

This should show the output as "Successfully added" along with entered input



Step 3: In the Form UI, Enter a large incorrect input. (Eg: ABCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCE)

This should show the output as "Invalid name" along with entered input.



||Part 2: Exploitation of ms package using ReDoS Attack.||

We have implemented a simple TODO application that uses the npm package humanize-ms of version: 1.0.1 which uses the ReDoS vulnerable version (0.6.2) of the ms package to convert the time entered by the user in human readable format (eg: 6 minutes) into milli seconds.

||OS used||: Ubuntu Linux 20.4 Lts

||Installations required||: Node.js, npm 

The following steps can be followed to run the application and perform the ReDoS atack:

Step 1: Install dependencies:

	 From a terminal open the location of the project: redos_ms_package and run the following command:
	 	
	 	npm install
	 	
Step 2: Build the Application:

	From the same location run the following of to build the application:
	
		npm run build
		
Step 3: Start the Application:

		npm start
		

Step 4: In the TODO Form UI, Enter an extremely large time input which is incorrect in its last position.
	
	
	An example of such an input is given in the file: input_for_redos.txt under the source folder.
	
	The content of this file can be simply copied and pasted into the input field on the UI.
	
Step 5: After entering the input, click submit.


This should hang the application due to the ReDoS Attack.


|| Solution using a rectified version of the package ||


We have implemented the same application with a version of the humanize-ms package (1.2.1) which uses the rectified version of the ms package(2.0.0). The same input can be used in this rectified application and the ReDoS Attack will no longer happen. To start the solution application the same steps given above can be followed from the project folder location: redos_ms_package_solved.

It can be seen that in the rectified application the ReDoS atack does not happen and the application no longer crashes.



 
