#Step-by-step guide to setting up a Grunt workflow
This guide assumes you have installed Grunt and Node.js to your system.

Jump down to *Summary* at the bottom of this file for a brief look at the simplified, better workflow rather than getting any details or context.

#Step 1: Create your `package.json` file
### `which npm`
Shows the location of npm

### `npm init`
> This utility will walk you through creating a `package.json` file.
> It only covers the most common items, and tries to guess sensible defaults.
> See `npm help json` for definitive documentation on these fields and exactly what they do.
> Use `npm install <pkg> --save` afterwards to install a package and save it as a dependency in the `package.json` file.
The utility will now prompt you to fill in the following, line-by-line. Defaults are provided:
> Press `^C` at any time to quit.
```
name: (src)
version: (1.0.0)
description: my grunt demo
entry point: (index.js)
test command: 
git repository:
keywords: grunt, keywords
author: (authorname)
license: (ISC)
About to write to C:\<PATH>
``` 
Then it will printout a JSON-formatted preview for you to respond to with yes or no.

```
{
	"name": "(grunt-workflow-demo)",
	"version": "1.0.0",
	"description": "my grunt demo",
	"main": "index.js",
	"scripts": {
		"test": "echo \"Error: no test specified\" && exit 1"
	}
	"keywords": [
		"grunt",
		"keywords"
	],
	"author": "(Ghandi)",
	"license": "ISC"
}
Is this ok? (yes)
```
This creates a handy `package.json` file that anyone can use to install the dependencies necessary for your project using `npm install`.

#Step 2: Install Grunt for your project
The next step in setting up our workflow is to install Grunt using `npm install --save-dev grunt`. 
* The `--save-dev` in there tells npm to save this dependency to our package.json file as a *developer dependency*. *Developer dependencies* are anything that your website doesn't necessarily need to run but that you as a developer are going to use to develop your website, such as Grunt.
* Now we have Grunt, though it can't do anything exciting yet because we need a Gruntfile.

#Step 3: Create your `Gruntfile.js`
`touch Gruntfile.js`
You can open this empty file in a text editor like Sublime.
On Mac you can type `subl .`, but my Mac has passed on.

#Step 4: Install necessary plug-ins for your project.
[Where to find plug-ins](http://gruntjs.com/plugins)

#Step 4 Example: grunt-sass
##Install
`$ npm install --save-dev grunt-sass`

#Step 5: Load Grunt module in `Gruntfile.js` using a file wrapper
In your `Gruntfile.js`:

```
module.exports = function(grunt){
	grunt.loadNpmTasks('plugin-name-here');
}
```

#Step 6: Load your plugins
```
module.exports = function(grunt){
	grunt.loadNpmTasks('plugin-name-here');

}
```

#Step 7: Configure your tasks
```
module.exports = function(grunt){
	grunt.loadNpmTasks('plugin-name-here');

	grunt.initConfig({
		
		});
}
```

#Step 8: Create a task
```
module.exports = function(grunt){
	grunt.loadNpmTasks('plugin-name-here');

	grunt.initConfig({
		name-of-configuration:	
			~~Configure your modules~~
				
			}
		});

	grunt.registerTask('name-of-task', [
		name-of-configuration
	])
}
```


#Step 8 Example: grunt-sass

```
module.exports = function(grunt){
	grunt.loadNpmTasks('grunt-sass');

	grunt.initConfig({
			sass: {
				dist: {
					src: 'src/sass/style.scss', #original scss file to process
					dest: 'dist/css/style.css' #destination folder doesn't need to exist yet
				}
			}
		});

	grunt.registerTask('default',[
		'sass'
	])
}
```

#Step 9: Do your task by simply running it with `grunt` in your directory.

#Step 9 Example: Run `sass` task with `grunt`:
```
> grunt
Running "sass:dist" (sass) task

Done, without errors.
```

This created the `dist/css/` folder with `style.css` in it, which is the `style.scss` Sass file converted into CSS.


#Step 10: Adding more tasks (using the previous examples)
Using that same Gruntfile, we're going to add in more tasks to show off what this can do.

##Merge two JavaScript files using `grunt-contrib-concat`
Run `npm install --save-dev grunt-contrib-concat` to install the plug-in.

Write it into the Gruntfile so that it looks like:

```
module.exports = function(grunt){
	grunt.loadNpmTasks('grunt-sass');
	grunt.loadNpmTasks('grunt-contrib-concat')
	grunt.initConfig({
			sass: {
				dist: {
					src: 'src/sass/style.scss', #original scss file to process
					dest: 'dist/css/style.css' #distribution folder doesn't need to exist yet
				}
			},
			concat: {
				dist: {
					src: 'src/js/*.js' #this is called globbing; we are asking it to find all .js file in this folder
					dest: 'dist/js/app.js'

				}
			}
		});

	grunt.registerTask('default',[
		'sass',
		'concat'
	])
}
```
Be sure to delete my comments because I am not using the actual method of writing comments and this will not work at all.

Again, all of these tasks will run with the humble `grunt` command. Since I already had it do `sass`, it only performed `concat` for me.

**You can also ask it to run only the **`concat` **task using **`grunt concat` **alone**.

#Step 11: Don't get overwhelmed with your huge Gruntfiles, using 
`load-grunt-tasks`
This will make the process of adding new tasks not only less repetitive, but also less confusing and overwhelming.

1. Run `npm install --save-dev load-grunt-tasks`
2. Replace all of the lines with `grunt.loadNpmTasks(...)` and replace them with one happy little line, `require('load-grunt-tasks`)(grunt);`:

```
module.exports = function(grunt){
	
	require('load-grunt-tasks')(grunt);

	grunt.initConfig({
			sass: {
				dist: {
					src: 'src/sass/style.scss', #original scss file to process (list of files also okay!)
					dest: 'dist/css/style.css' #distribution folder doesn't need to exist yet
				}
			},
			concat: {
				dist: {
					src: 'src/js/*.js' #this is called globbing; we are asking it to find all .js file in this folder
					dest: 'dist/js/app.js'

				}
			}
		});

	grunt.registerTask('default',[
		'sass',
		'concat'
	])
}
```

This will import any Grunt dependencies it can find in our directory. No more installing plug-ins!

#Step 12: Lint your file
This will help proofread your file in case anything is amiss/typoed.

`npm install --save-dev grunt-contrib-jshint`

Add task to your list of tasks:
```
jshint: {
	all:[
		'Gruntfile.js',
		config.jsSrcDir+"*.js"
		]
}
```
And of course, register this task:
```
grunt.registerTask('jshint',[other tasks]);
```

This will give us warnings if we're missing something critical, like, say, a semi-colon. For this somewhat obvious reason, be sure to call `'jshint'` first by registering it first.

##`jshint` special rules

You can specify special lint rules with
```
	jshint: {
		options: {
			your special rules here
		},
		all: [
			directories to apply all lint rules to
		]
	}
```

###Example: force triple equal signs
This is actually a built-in function called `'eqeqeq'`.
```
	jshint: {
		options: {
			'eqeqeq': true
		},
		all: [
			'Gruntfile.js',
			'/source/directory/*.js'
		]
	}
```

#Helpful Knowledge: Watchtasks
Sometimes you just want to focus on coding, and you want your Grunt tasks to just run for you when, say, you save the JavaScript file you were just working on. Running `grunt` is just such a **chore**, right?

Well, as you might have expected, there's a plug-in for that.
`npm install --save-dev grunt-contrib-watch`

Configure your Watchtask with the files you want watching:
```
...
	watch: {
		sass: {
			files: config.scssDir+'**/*.scss'
			tasks: ['sass']
		}
	}
});

	grunt.registerTask('default',[
		'jshint',
		'watch',
		everything else
		])
```

#Final Tip: Handling many directories
It can get a little clunky handling many different sources and paths, especially if you want to rename one across many, many tasks. You can create a new file with `touch Gruntfile.yml` to hold a list of all of your directories.

Example of `Gruntconfig.yml` for the previous example tasks:
```
scssDir: src/sass
jsSrcDir: src/js/
jsConcatDir: dist/js
cssDir: dist/css
```
In your `Gruntfile.js`, you can import this configuration using simply: 
```
var config = grunt.file.readYAML('Gruntconfig.yml') 
```

Then edit the paths to match the variables:
```
	grunt.initConfig({
			sass: {
				dist: {
					src: config.scssDir+'style.scss',
					dest: config.cssDir+'style.css'
				}
			},
			concat: {
				dist: {
					src: config.jsSrcDir+'*.js',
					dest: config.jsConcatDir+'app.js'

				}
			}
		});

	grunt.registerTask('default',[
		'sass',
		'concat'
	])
}
```

#Summary
0. Be in desired directory
1. `npm init` > fill in information > `yes`
2. `npm install --save-dev grunt`
3. `touch Gruntfile.js`
4. `npm install --save-dev load-grunt-tasks`
5. For each plug-in needed for your task:
> `npm install --save-dev task-name`
7. `npm install -save-dev grunt-config-jshint` to catch any errors and, if found, abort your tasks
8. (optional) Create a list of folders and their nicknames you will be using to run your tasks and save it in a file called Gruntconfig.yml (see final tip, above this Summary)
9. (optional) `npm install --save-dev grunt-contrib-watch`, then follow my instructions above to define and register your Watchtasks for automatic Grunt task executions.
10. Open and edit Gruntfile and enter/fill out:

```
module.exports = function(grunt){
	
	require('load-grunt-tasks')(grunt);

	grunt.initConfig({
			jshint: {
				options: {
					optional! you can specify any other rules you'd like caught over here; if not, just delete this text and the options: { }, containing it
					},
				all: [
						'Gruntfile.js',
						any other relevant source paths
					]
			},
			task2: {
				dist: {
					src: 'SOURCE/PATH/2'
					dest: 'DISTRIBUTION/PATH/2'
				}
			},
			task3: {
				dist: {
					src: ['SOURCE/PATH/3A.js','SOURCE/PATH/3B.js']
					dest: 'DISTRIBUTION/PATH/3'
				}
			}
		});

	grunt.registerTask('default',[
		'task1',
		'task2',
		'task3'
	])
}
```
11. Save and run from your directory with `grunt` for all tasks or, for example, `grunt task1` for a single task.