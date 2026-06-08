/**
 * card-renderer.js
 *
 * Fetches data.json from the same directory as the calling page,
 * then renders card elements into #card-container.
 *
 * Usage: each page calls initCards({ type: 'potions' | 'mishaps' })
 */

async function initCards({ type }) {
  const container = document.getElementById('card-container');
  if (!container) {
    console.error('card-renderer: no #card-container element found.');
    return;
  }

  // Fetch the data file relative to the current page
  let data;
  try {
    const response = await fetch('./data.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    data = await response.json();
  } catch (err) {
    container.innerHTML = `<p style="color:red;">Failed to load card data: ${err.message}</p>`;
    return;
  }

  // Build the grid
  const grid = document.createElement('div');
  grid.className = `card-grid ${type}`;

  for (const item of data) {
    const card = buildCard(type, item);
    grid.appendChild(card);
  }

  container.appendChild(grid);
}

/**
 * Dispatches to the correct card builder based on type.
 */
function buildCard(type, item) {
  switch (type) {
    case 'potions': return buildPotionCard(item);
    case 'mishaps': return buildMishapCard(item);
    default:
      console.warn(`card-renderer: unknown type "${type}"`);
      return document.createElement('div');
  }
}

/**
 * Builds a potion card element.
 * Expected fields: name (string), ingredients (string[]), effect (string)
 */
function buildPotionCard({ name = 'Unnamed', ingredients = [], effect = '' }) {
  const card = document.createElement('div');
  card.className = 'card potion';

  const nameEl = document.createElement('div');
  nameEl.className = 'card-name';
  nameEl.textContent = name;
  card.appendChild(nameEl);

  // Ingredients
  const ingLabel = document.createElement('div');
  ingLabel.className = 'card-label';
  ingLabel.textContent = 'Ingredients';
  card.appendChild(ingLabel);

  const ingList = document.createElement('ul');
  ingList.className = 'ingredients-list';
  for (const ingredient of ingredients) {
    const li = document.createElement('li');
    li.textContent = ingredient;
    ingList.appendChild(li);
  }
  card.appendChild(ingList);

  // Effect
  const effectLabel = document.createElement('div');
  effectLabel.className = 'card-label';
  effectLabel.textContent = 'Effect';
  card.appendChild(effectLabel);

  const effectEl = document.createElement('div');
  effectEl.className = 'card-value';
  effectEl.textContent = effect;
  card.appendChild(effectEl);

  return card;
}

/**
 * Builds a mishap card element.
 * Expected fields: name (string), effect (string)
 */
function buildMishapCard({ name = 'Unnamed', effect = '' }) {
  const card = document.createElement('div');
  card.className = 'card mishap';

  const nameEl = document.createElement('div');
  nameEl.className = 'card-name';
  nameEl.textContent = name;
  card.appendChild(nameEl);

  const effectLabel = document.createElement('div');
  effectLabel.className = 'card-label';
  effectLabel.textContent = 'Effect';
  card.appendChild(effectLabel);

  const effectEl = document.createElement('div');
  effectEl.className = 'card-value';
  effectEl.textContent = effect;
  card.appendChild(effectEl);

  return card;
}
