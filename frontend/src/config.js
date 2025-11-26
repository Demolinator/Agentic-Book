/**
 * Frontend configuration for API base URL.
 * Defaults to localhost for development.
 */
const config = {
  API_BASE_URL: process.env.API_BASE_URL || 'http://localhost:8000',
};

export default config;

