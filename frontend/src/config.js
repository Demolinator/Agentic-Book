/**
 * Frontend configuration for API base URL.
 * Defaults to localhost for development.
 * 
 * Note: In browser environment, process.env is not available.
 * For production, you can set window.API_BASE_URL before this module loads,
 * or configure it via Docusaurus's customFields in docusaurus.config.js
 */
const getApiBaseUrl = () => {
  // Check if running in browser and window variable is set
  if (typeof window !== 'undefined' && window.API_BASE_URL) {
    return window.API_BASE_URL;
  }
  
  // Default to localhost for development
  // In production, this should be set via window.API_BASE_URL or docusaurus.config.js
  return 'http://localhost:8000';
};

const config = {
  API_BASE_URL: getApiBaseUrl(),
};

export default config;

