/**
 * card-renderer.js
 *
 * Fetches data.json from the same directory as the calling page,
 * then renders card elements into #card-container.
 *
 * Usage: each page calls initCards({ type: 'potions' | 'mishaps' | 'characters' })
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
    case 'characters': return buildCharacterCard(item);
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
 * Builds a character card element.
 * Expected fields: name (string), subtitle (string, optional), body (string with **bold** support)
 */
function buildCharacterCard({ name = 'Unnamed', subtitle = '', body = '' }) {
  const card = document.createElement('div');
  card.className = 'card character';

  const nameEl = document.createElement('div');
  nameEl.className = 'card-name';
  nameEl.textContent = name;
  card.appendChild(nameEl);

  if (subtitle) {
    const subEl = document.createElement('div');
    subEl.className = 'card-subtitle';
    subEl.textContent = subtitle;
    card.appendChild(subEl);
  }

  if (body) {
    const bodyEl = document.createElement('div');
    bodyEl.className = 'card-body';
    // Convert **text** to <strong>text</strong>, preserve whitespace via CSS
    bodyEl.innerHTML = body
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');
    card.appendChild(bodyEl);
  }

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
