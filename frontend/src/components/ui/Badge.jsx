import React from 'react';

export const Badge = ({ children, variant = 'brand', size = 'md', className = '' }) => {
  const baseClasses = 'inline-flex items-center font-medium rounded-full transition-colors';
  
  const sizeClasses = {
    sm: 'text-xs px-2.5 py-0.5 gap-1.5',
    md: 'text-xs px-3 py-1 gap-2',
    lg: 'text-sm px-4 py-1.5 gap-2',
  };

  const variantClasses = {
    brand: 'bg-brand-500/15 text-brand-400 border border-brand-500/30',
    fatal: 'bg-red-500/15 text-red-400 border border-red-500/30',
    warning: 'bg-amber-500/15 text-amber-400 border border-amber-500/30',
    success: 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30',
    info: 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30',
    purple: 'bg-purple-500/15 text-purple-400 border border-purple-500/30',
    neutral: 'bg-navy-800 text-slate-300 border border-navy-700',
  };

  return (
    <span className={`${baseClasses} ${sizeClasses[size] || sizeClasses.md} ${variantClasses[variant] || variantClasses.brand} ${className}`}>
      {children}
    </span>
  );
};
