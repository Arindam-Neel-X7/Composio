const fs = require('fs');
let content = fs.readFileSync('outputs/task-18/human_recheck_form.html', 'utf8');

// Test 1: with default filter 'corrected'
function runWithFilter(filterVal) {
  let modified = content.replace("let currentFilter = 'corrected';", `let currentFilter = '${filterVal}';`);
  const start = modified.indexOf('<script>');
  const end = modified.lastIndexOf('</script>');
  const script = modified.substring(start + 8, end);

  let cards = [];
  global.document = {
    getElementById: (id) => ({
      innerHTML: '',
      appendChild: (el) => { cards.push(el); },
      value: '',
      textContent: '',
      style: {},
      addEventListener: () => {}
    }),
    querySelectorAll: () => [],
    createElement: () => ({
      className: '',
      id: '',
      innerHTML: '',
      dataset: {},
      appendChild: () => {},
      querySelectorAll: () => [],
      querySelector: () => ({ value: '', addEventListener: () => {} })
    })
  };
  global.localStorage = { getItem: () => null, setItem: () => {} };
  global.window = {};

  eval(script);
  return cards.length;
}

console.log("Filter 'corrected':", runWithFilter('corrected'), "cards rendered");
console.log("Filter 'all':", runWithFilter('all'), "cards rendered");
