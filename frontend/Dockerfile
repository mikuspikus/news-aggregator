# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /frontend

# add `/frontend/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache frontend dependencies
COPY package.json /frontend/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# start frontend
CMD ["npm", "run", "serve"]
