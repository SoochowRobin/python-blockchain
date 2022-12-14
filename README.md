The blockchain is a list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between blocks.

Some basic python concepts:
A python module is a file that contains various Python definitions and statements. 

Mininig blocks refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. 
The <b>genesis block</b> is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain. 

Encoding is the process of converting data into a particular format (such as the utf-8 format). For example, encoding a string in utf-8, would produce the equivalent byte string in utf-8 characters. Decoding converts the encoded data back into its original form.


The entire project could be divided into several sections:

Section 2: Test the application
Listed required python package for this project, and other developers could jusr run 'pip3 install -r requirements.txt'. Continuous update requirements.txt file to make future collaboration as easy as possible. 


**Activate the vitural environment**
```
source blockchain-env/bin/activate
```

**Install all package**
```
pip3 install -r requirements.txt 
```

**Run the tests**
Make sure to activate the vitural environment.

```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual environment

```
python3 -m backend.app
```


**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app
```

**Run the frontend**
In the frontend directory:
```
npm run start 
```

**Seed the backend with data**
Make sure to activate the virtual environment.
```
export SEED_DATA = True && Python3 -m backend.app
```

# Section Summary for Each Part

### `Python Fundamentals`

Here's a list that highlights the main lessons from the section: 
Functions in python are mechanism to re-execute lines of code encapsulated within the function body. Functions return output values, usually based on one or more inputs. They also have side effects - portions of the function (like prints) that don't affect the return value. 

Comparison operators allow you to control the execution of your code by comparing two values and returning a boolean result. For example, to check if two values are equal, use: ==. Or to check if a value is greater than or equal to, use: >=. 

### `Blockchain Application`

The blockchain is list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between between blocks. In a blockchain that supports a cryptocurrency, blocks store transactions. 

A python module is a file that contains various Python definitions and statements. For example, the block.py file serves as the block module for the project. The __name__ value in Python reflects the name of the module it's used within, except when the file is directly executed. When a file is directly executed the __name__ value becomes '__main__'. 

Mining blocks refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. We'll expand on this in the section on Proof of Work. 

The genesis block is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain. 

A hashing algorithm generates a unique output for every unique output. In the case of this project, we're using the sha-256 algorithm, which produces a unique 256 character hash in binary, and a 64 character hash in hexadecimal. 

Encoding is the process of converting data into a particular format (such as the utf-8 format). For example, encoding a string in utf-8, would produce the equivalent byte string in utf-8 characters. Decoding converts the encoded data back into its original form. 

A lambda in python is a function that can be declared inline. In the project so far, we've used it for the map() method which can transform a list into a new list. The map function's first parameter is a lambda, which defines how to transform each item in the original list to produce the new list. 










# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
