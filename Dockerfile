# Extend base Slidev image
FROM tangramor/slidev:latest

# Set environment for npm cache to avoid /.npm permission issue
ENV HOME=/home/node \
    NPM_CONFIG_CACHE=/home/node/.npm

# Set working directory
WORKDIR /slidev

# Create a default package.json if needed (prevents install errors)
COPY package.json package-lock.json* ./

# Install plotly.js-dist
RUN npm install plotly.js-dist

# Expose default Slidev port
EXPOSE 3030

# Default command to launch Slidev
CMD ["npx", "slidev", "--remote"]
