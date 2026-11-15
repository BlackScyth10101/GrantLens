/**
 * GrantLens Centralized API Configuration
 * Standardized to IPv4 loopback (127.0.0.1) to avoid IPv6 (::1) localhost resolution mismatches
 */
export const API_BASE = 'http://127.0.0.1:8000';

/**
 * Extracts a human-readable error message from backend API error responses,
 * preventing '[object Object]' when FastAPI returns validation error arrays.
 */
export const extractErrorMessage = (data, defaultMessage = 'An unexpected error occurred.') => {
  if (!data) return defaultMessage;
  if (typeof data === 'string') return data;
  if (typeof data.detail === 'string') return data.detail;
  if (Array.isArray(data.detail)) {
    return data.detail.map((item) => item.msg || JSON.stringify(item)).join('; ');
  }
  if (data.detail && typeof data.detail === 'object') {
    return data.detail.msg || JSON.stringify(data.detail);
  }
  if (data.message && typeof data.message === 'string') return data.message;
  return defaultMessage;
};

