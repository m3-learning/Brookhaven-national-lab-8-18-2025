# Extend base Slidev image
FROM tangramor/slidev:latest

# Set environment to avoid global cache issues
ENV HOME=/home/node \
    NPM_CONFIG_CACHE=/home/node/.npm

# Set working directory
WORKDIR /slidev

# Copy files as root
COPY package.json package-lock.json* ./

# 👇 Fix permissions BEFORE switching to node
RUN chown -R node:node /slidev

# 👇 Now switch to non-root user
USER node

# Safe to install now
RUN npm install plotly.js-dist qrcode.vue

# Expose Slidev port
EXPOSE 3030

# Default command
CMD ["npx", "slidev", "--remote"]
