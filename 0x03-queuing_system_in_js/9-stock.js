import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';


const client = createClient();
const app = express();
const port = 1245;

client.on('connect', () => {
  console.log('Redis client connected to the server');
}).on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const get = promisify(client.get).bind(client);

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

function getItemById(id) {
  return listProducts.filter((item) => item.id === id)[0];
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await get(itemId);
  return stock;
}


app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async function (req, res) {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (item) {
    const currentStock = await getCurrentReservedStockById(itemId);
    const response = {
      "itemId": item.id,
      "itemName": item.name,
      "price": item.price,
      "initialAvailableQuantity": item.stock,
      "currentQuantity": currentStock !== null ? parseInt(currentStock) : item.stock
    };
    res.json(response);
  } else {
    res.json({"status": "Product not found"});
  }
});

app.get('/reserve_product/:itemId', async function (req, res) {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.json({"status": "Product not found"});
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock !== null) {
    if (currentStock > 0) {
      reserveStockById(itemId, currentStock - 1);
      res.json({"status": "Reservation confirmed", "itemId": itemId});
    } else {
      res.json({"status": "Not enough stock available", "itemId": itemId});
    }
  } else {
    reserveStockById(itemId, item.stock - 1);
    res.json({"status": "Reservation confirmed", "itemId": itemId});
  }
});


app.listen(port, () => {
  console.log(`app listening at 127.0.0.1:${port}`);
});
