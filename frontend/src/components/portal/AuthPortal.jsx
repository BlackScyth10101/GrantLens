import React, { useState } from 'react';
import { 
  ShieldCheck, 
  Lock, 
  Mail, 
  Building2, 
  GraduationCap, 
  User, 
  ArrowRight, 
  AlertCircle, 
  Loader2, 
  Eye, 
  EyeOff 
} from 'lucide-react';

export default function AuthPortal({ onAuthSuccess, onCancel }) {
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);
  const [showPassword, setShowPassword] = useState(false);

  const [formData, setFormData] = useState({
    email: '',
    password: '',
    fullName: '',
    institution: '',
    department: '',
  });

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
    if (errorMessage) setErrorMessage(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage(null);
    setSuccessMessage(null);

    const endpoint = isLogin 
      ? 'http://localhost:8000/api/v1/auth/login' 
      : 'http://localhost:8000/api/v1/auth/register';

    const payload = isLogin 
      ? { email: formData.email, password: formData.password }
      : {
          email: formData.email,
          password: formData.password,
          full_name: formData.fullName,
          institution: formData.institution,
          department: formData.department || undefined,
        };

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Authentication request failed.');
      }

      if (isLogin) {
        localStorage.setItem('grantlens_token', data.access_token);
        localStorage.setItem('grantlens_user', JSON.stringify(data.user));
        if (onAuthSuccess) onAuthSuccess(data.user, data.access_token);
      } else {
        // Auto-switch to login on successful registration
        setIsLogin(true);
        setSuccessMessage('Account provisioned successfully. You can now sign in.');
      }
    } catch (err) {
      setErrorMessage(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSSOLogin = () => {
    setLoading(true);
    setTimeout(() => {
      setErrorMessage('Redirecting to University Shibboleth / InCommon Identity Provider...');
      setLoading(false);
    }, 1200);
  };

  return (
    <div className="min-h-[85vh] flex flex-col justify-center items-center px-4 py-8 relative">
      {/* Background radial glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-brand-500/10 rounded-full blur-[140px] pointer-events-none" />

      {/* Main card */}
      <div className="w-full max-w-md bg-navy-900/90 border border-navy-700/80 rounded-2xl p-8 backdrop-blur-xl shadow-2xl relative z-10">
        {/* Brand identity */}
        <div className="flex flex-col items-center mb-6">
          <div className="w-12 h-12 rounded-xl bg-gradient-to-tr from-brand-600 to-brand-400 flex items-center justify-center shadow-lg shadow-brand-500/20 mb-3">
            <ShieldCheck className="w-7 h-7 text-white" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-white">Researcher Portal</h1>
          <p className="text-xs text-slate-400 mt-1">Institutional Pre-Submission Audit Clearance</p>
        </div>

        {/* Tab switch */}
        <div className="flex bg-navy-950 rounded-xl p-1 mb-6 border border-navy-800">
          <button
            type="button"
            onClick={() => { setIsLogin(true); setErrorMessage(null); setSuccessMessage(null); }}
            className={`flex-1 py-2 text-xs font-semibold rounded-lg transition-all ${
              isLogin 
                ? 'bg-brand-500 text-slate-950 shadow-md font-bold' 
                : 'text-slate-400 hover:text-white'
            }`}
          >
            Sign In
          </button>
          <button
            type="button"
            onClick={() => { setIsLogin(false); setErrorMessage(null); setSuccessMessage(null); }}
            className={`flex-1 py-2 text-xs font-semibold rounded-lg transition-all ${
              !isLogin 
                ? 'bg-brand-500 text-slate-950 shadow-md font-bold' 
                : 'text-slate-400 hover:text-white'
            }`}
          >
            Create Account
          </button>
        </div>

        {/* Success message banner */}
        {successMessage && (
          <div className="mb-5 p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-start gap-2.5 text-xs text-emerald-300">
            <span>{successMessage}</span>
          </div>
        )}

        {/* Error notification banner */}
        {errorMessage && (
          <div className="mb-5 p-3 rounded-lg bg-red-500/10 border border-red-500/30 flex items-start gap-2.5 text-xs text-red-300">
            <AlertCircle className="w-4 h-4 shrink-0 text-red-400 mt-0.5" />
            <span>{errorMessage}</span>
          </div>
        )}

        {/* Primary form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          {!isLogin && (
            <>
              <div>
                <label className="block text-xs font-medium text-slate-300 mb-1">Full Legal Name</label>
                <div className="relative">
                  <User className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
                  <input
                    type="text"
                    name="fullName"
                    required
                    value={formData.fullName}
                    onChange={handleChange}
                    placeholder="Prof. Jane Doe"
                    className="w-full bg-navy-950 border border-navy-800 rounded-lg pl-9 pr-3 py-2 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-medium text-slate-300 mb-1">Institution</label>
                <div className="relative">
                  <Building2 className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
                  <input
                    type="text"
                    name="institution"
                    required
                    value={formData.institution}
                    onChange={handleChange}
                    placeholder="Stanford University"
                    className="w-full bg-navy-950 border border-navy-800 rounded-lg pl-9 pr-3 py-2 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-medium text-slate-300 mb-1">Department</label>
                <div className="relative">
                  <GraduationCap className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
                  <input
                    type="text"
                    name="department"
                    value={formData.department}
                    onChange={handleChange}
                    placeholder="Department of Computer Science"
                    className="w-full bg-navy-950 border border-navy-800 rounded-lg pl-9 pr-3 py-2 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
                  />
                </div>
              </div>
            </>
          )}

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">Institutional Email</label>
            <div className="relative">
              <Mail className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
              <input
                type="email"
                name="email"
                required
                value={formData.email}
                onChange={handleChange}
                placeholder="researcher@university.edu"
                className="w-full bg-navy-950 border border-navy-800 rounded-lg pl-9 pr-3 py-2 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">Password</label>
            <div className="relative">
              <Lock className="absolute left-3 top-3 w-4 h-4 text-slate-500" />
              <input
                type={showPassword ? 'text' : 'password'}
                name="password"
                required
                minLength={8}
                value={formData.password}
                onChange={handleChange}
                placeholder="••••••••••••"
                className="w-full bg-navy-950 border border-navy-800 rounded-lg pl-9 pr-10 py-2 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-3 text-slate-500 hover:text-slate-300"
              >
                {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full mt-2 py-2.5 px-4 rounded-lg bg-brand-500 hover:bg-brand-400 text-slate-950 font-semibold text-sm flex items-center justify-center gap-2 shadow-lg shadow-brand-500/20 disabled:opacity-50 transition-all cursor-pointer"
          >
            {loading ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <>
                <span>{isLogin ? 'Sign In to Workspace' : 'Complete Registration'}</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </form>

        {/* Institutional SSO divider */}
        <div className="relative my-6 text-center">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-navy-800" />
          </div>
          <span className="relative px-3 bg-navy-900 text-[11px] font-medium text-slate-500 uppercase tracking-wider">
            Or Federated Access
          </span>
        </div>

        {/* SSO Action */}
        <button
          type="button"
          onClick={handleSSOLogin}
          disabled={loading}
          className="w-full py-2.5 px-4 rounded-lg bg-navy-800 hover:bg-navy-750 border border-navy-700/60 text-slate-200 text-xs font-semibold flex items-center justify-center gap-2 transition-all cursor-pointer"
        >
          <Building2 className="w-4 h-4 text-cyan-400" />
          <span>Single Sign-On (InCommon / EduGAIN SAML)</span>
        </button>

        {onCancel && (
          <button
            type="button"
            onClick={onCancel}
            className="w-full mt-4 text-center text-xs text-slate-400 hover:text-slate-200 transition-colors"
          >
            ← Back to Public Overview
          </button>
        )}

        {/* Confidentiality footer badge */}
        <p className="text-[11px] text-slate-500 text-center mt-6 flex items-center justify-center gap-1.5">
          <Lock className="w-3 h-3 text-emerald-400" />
          <span>Protected under FERPA & Non-Disclosure Compliance Protocols</span>
        </p>
      </div>
    </div>
  );
}
