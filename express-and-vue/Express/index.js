import express, { Router } from 'express';
import { json, urlencoded } from 'body-parser';
import morgan from 'morgan';
import { join } from 'path';
import expressVue from 'express-vue';
import restController from './helpers/rest-controller';
import { RESPONSE, MESSAGES, MAX_FILE_SIZE, VUE_OPTIONS } from './helpers/constants';
import env from './config/environment';

const { ERROR, NOT_FOUND } = RESPONSE;

const app = express();
const api = Router();

app.use(expressVue.init(VUE_OPTIONS));

app.get('/', (req, res) => {
  res.renderVue('App.vue');
});

app.use('/public', express.static(join(__dirname, '../../public'));
app.use('/static', express.static('static'));
app.use(urlencoded({ limit: MAX_FILE_SIZE.size, defer: true, extended: true }));
app.use(json({ limit: MAX_FILE_SIZE.size }));

if(!env('NODE_ENV', 'production')) {
  app.use(morgan('dev'));
}

app.use('/api', restController(api));

app.use((req, res, next) => {
  let err = new Error(MESSAGES[NOT_FOUND]);
  err.status = NOT_FOUND;
  next(err);
});

app.use((err, req, res, next) => {
  const defaultCase = new Error(MESSAGES[ERROR]);
  err.status = err.status || ERROR;
  defaultCase.status = ERROR;
  res.status(err.status || defaultCase.status).renderVue('Error.vue', {
    errorMsg: err.message || defaultCase.message,
    error: err || defaultCase
  });
});

const server = app.listen(env('PORT') || 8080, () => console.log('Listening to port %d', server.address().port));