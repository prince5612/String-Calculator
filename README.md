<!DOCTYPE html>
<html lang="en">
<!-- <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced String Calculator - README</n>
  <style>
    body { font-family: Arial, sans-serif; background: #f9f9f9; color: #333; padding: 2rem; max-width: 800px; margin: auto; }
    h1, h2 { color: #2c3e50; }
    pre { background: #ecf0f1; padding: 1rem; border-radius: 4px; overflow-x: auto; }
    code { background: #ecf0f1; padding: 2px 4px; border-radius: 4px; }
    ul { line-height: 1.6; }
    .badge { display: inline-block; margin-right: 0.5rem; }
  </style>
</head> -->
<body>
  <h1>String Calculator</h1>
  <p>An interactive web-based calculator that parses string expressions with custom delimiters, inline operator switching, and ignores numbers > 1000.</p>
  <p><b></b>Read the pdf file given in Documents folder <b></b> to understand about the all test cases.</p>
  <h2>Features</h2>
  <ul>
    <li><strong>Flexible Delimiters</strong>: Define custom delimiters using <code> op[del1][del2]expression </code> syntax.</li>
    <li><strong>Leading Operator</strong>: Start with <code>+ - * / ^</code> to set the initial operation (defaults to <code>+</code>).</li>
    <li><strong>Inline Operator Switching</strong>: Change operators mid-expression using tokens (e.g., <code>1,+,2,*,3</code>).</li>
    <li><strong>Ignore Large Numbers</strong>: Excludes numbers greater than 1000 from calculation.</li>
    <li><strong>Error Handling</strong>: Detects invalid tokens, malformed headers, division by zero, and empty inputs.</li>
    <li><strong>Clean Output</strong>: Displays a numeric result.</li>
    <li><strong>History & Copy</strong>: Tracks the last 10 computations and allows copying the expression.</li>
  </ul>
 
  <h2>Technologies</h2>
  <span class="badge">Python</span>
  <span class="badge">Flask</span>
  <span class="badge">HTML/CSS</span>
  <span class="badge">JavaScript</span>
  <span class="badge">unittest</span>
  
  <h2>Usage</h2>
  <pre><code>python app.py
# Navigate to http://127.0.0.1:5000/ in your browser</code></pre>
  <h3>Sample Inputs</h3>
  <ul>
    <li><code>1,2,3</code></li>
    <li><code>*1,2,3</code></li>
    <li><code>[;][%]1;2%3</code></li>
    <li><code>1,+,2,*,3</code></li>
  </ul>
  <h2>Running Tests</h2>
  <pre><code>python -m unittest</code></pre>
  <h2>Project Structure</h2>
  <pre><code>.
├── app.py
├── calculator.py
├── test_calculator.py
├── Documents/String_Calculator_TestCases.pdf
├── templates/index.html
├── static/css/style.css
└── static/js/app.js
  </code></pre>
</body>
</html>
