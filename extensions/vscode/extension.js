const fetch = require('node-fetch');

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "vizio" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('vizio.helloWorld', function () {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from vizio!');
	});

	context.subscriptions.push(disposable);
}

vscode.commands.registerCommand("vizio.generateFlowchart", async () => {
	// Get the active text editor
	const editor = vscode.window.activeTextEditor;

	if (editor) {
		const selectedText = editor.document.getText(editor.selection);

		vscode.window.showInformationMessage("vizio: Generating flowchart...");
		const { data } = await getSvg(selectedText);
		const dotContent = data.results;
		showSvg(dotContent);
	}
});

function getSvg(code) {
	return new Promise((resolve) => {
		return fetch("https://b3rmosfql9.execute-api.ap-southeast-1.amazonaws.com/generate_viz_devs", {
			method: "POST",
			body: JSON.stringify({ source_code: code }),
		})
			.then(response => response.json())
			.then(data => resolve({ data }));
	});
}

function showSvg(dotContent) {
	vscode.window.showInformationMessage("vizio: Showing flowchart...");
	const dotFilePath = vscode.Uri.parse(`untitled:${"flowchart.dot"}`);
	vscode.workspace.openTextDocument(dotFilePath).then((a) => {
		vscode.window.showTextDocument(a, 1, false).then((e) => {
			e.edit((editBuilder) => {
				editBuilder.insert(new vscode.Position(0, 0), dotContent);
			}).then(() => {
				vscode.commands.executeCommand("graphviz-interactive-preview.preview.beside");
			});
		});
	});

	vscode.window.showInformationMessage("vizio: Flowchart generated!");
}

// This method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
