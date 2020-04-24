import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8080/'
  // ,
  // headers: {
  //   'Access-Control-Allow-Origin': '*',
  //   'Content-Type': 'application/x-www-from-urlencoded'
  // }
})