import React from 'react';

export const Button = ({
  children,
  variant = 'primary',
  size = 'md',
  className = '',
  icon: Icon,
  iconPosition = 'left',
  onClick,
  disabled = false,
  ...props
}) => {
  const baseClasses = 'inline-flex items-center justify-center font-medium transition-all duration-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/50 disabled:opacity-50 disabled:pointer-events-none active:scale-[0.98] cursor-pointer';

  const sizeClasses = {
    sm: 'text-xs px-3 py-1.5 gap-1.5 font-medium',
    md: 'text-sm px-4 py-2 gap-2 font-medium',
    lg: 'text-base px-6 py-3 gap-2.5 font-semibold',
    pill: 'text-sm px-5 py-2.5 rounded-full gap-2 font-semibold',
    'pill-lg': 'text-base px-7 py-3.5 rounded-full gap-2.5 font-semibold',
  };

  const variantClasses = {
    primary: 'bg-gradient-to-r from-brand-500 to-brand-600 hover:from-brand-600 hover:to-brand-700 text-white shadow-glow-brand hover:shadow-glow-brand-lg border border-brand-400/30',
    secondary: 'bg-navy-800/90 hover:bg-navy-750 text-slate-200 hover:text-white border border-navy-700 hover:border-navy-600 backdrop-blur-sm',
    outline: 'bg-transparent text-brand-400 hover:text-brand-300 border border-brand-500/40 hover:border-brand-500/70 hover:bg-brand-500/10',
    ghost: 'bg-transparent hover:bg-navy-800 text-slate-300 hover:text-white',
    fatal: 'bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/40',
  };

  return (
    <button
      className={`${baseClasses} ${sizeClasses[size] || sizeClasses.md} ${variantClasses[variant] || variantClasses.primary} ${className}`}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {Icon && iconPosition === 'left' && <Icon className="w-4 h-4 shrink-0" />}
      {children}
      {Icon && iconPosition === 'right' && <Icon className="w-4 h-4 shrink-0" />}
    </button>
  );
};
