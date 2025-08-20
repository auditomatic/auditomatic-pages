# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based static website for **Auditomatic Lite**, a browser-based LLM evaluation tool. The site uses the Hugoplate theme (based on Hugo + Tailwind CSS v4) and serves as a documentation and landing page for the Auditomatic application.

## Architecture

### Hugo Site Structure
- **Content**: Markdown content in `content/english/` (multi-language ready)
- **Theme**: Uses Hugoplate theme in `themes/hugoplate/` (Git submodule)
- **Configuration**: Split config in `config/_default/` and main `hugo.toml`
- **Assets**: Static files in `assets/` and theme assets in `themes/hugoplate/assets/`
- **Generated**: Hugo builds to `public/` directory
- **Dependencies**: Uses Hugo modules defined in `go.mod`

### Key Directories
- `content/english/`: Main content (homepage, guides, blog posts)
- `layouts/`: Custom layout overrides (inherits from theme)
- `static/`: Static assets served at root
- `data/`: JSON data files for theme configuration
- `config/`: Split configuration files
- `tailwind-plugin/`: Custom Tailwind plugins

## Development Commands

### Primary Commands
```bash
# Install dependencies
npm install

# Development server with hot reload
npm run dev
# Equivalent: hugo server

# Production build
npm run build
# Equivalent: hugo --gc --minify --templateMetrics --templateMetricsHints --forceSyncStatic

# Preview production build
npm run preview
```

### Hugo Commands
```bash
# Direct Hugo commands (when npm not available)
hugo server                    # Development server
hugo --gc --minify            # Production build
```

### Theme Management
```bash
# Update Hugo modules
npm run update-modules

# Format code with Prettier
npm run format
# Note: Prettier configured for Go templates via prettier-plugin-go-template
```

## Content Management

### Adding Content
- Blog posts: `content/english/blog/`
- Guides/Documentation: `content/english/guides/`
- Pages: `content/english/pages/`
- Authors: `content/english/authors/`

### Homepage Configuration
- Main banner/features: `content/english/_index.md`
- Site params: `config/_default/params.toml`
- Theme settings: `data/theme.json`
- Social links: `data/social.json`

## Configuration Files

### Critical Config Files
- `hugo.toml`: Main Hugo configuration, plugins, build settings
- `config/_default/params.toml`: Site parameters, SEO, features
- `config/_default/menus.en.toml`: Navigation menus
- `config/_default/languages.toml`: Multi-language setup
- `go.mod`: Hugo modules and dependencies

### Theme Customization
- Override theme layouts in `layouts/`
- Custom CSS in `assets/css/custom.css`
- Custom JS in `static/js/`

## Build System

### Hugo + Tailwind Pipeline
- Hugo processes templates and content
- Tailwind CSS v4 handles styling
- Hugo modules provide reusable components
- AutoPrefixer for browser compatibility

### Asset Processing
- Images: Processed by Hugo's image processing
- CSS: Tailwind compilation handled by Hugo
- JS: Static files served from `static/js/`
- Fonts: Font Awesome included via theme modules

## Deployment

### Build Process
1. `npm run build` generates `public/` directory
2. Hugo processes all content and templates  
3. Tailwind compiles CSS with purging
4. Assets are optimized and minified

### Static Hosting
- Built for static hosting (Netlify, Vercel, GitHub Pages)
- No server-side dependencies
- All content pre-generated at build time

## Development Notes

- Uses Hugoplate theme as Git submodule
- Tailwind v4 configuration in `tailwind-plugin/`
- Hugo Extended required for SCSS/PostCSS processing
- Go modules handle theme dependencies automatically
- Prettier formatting includes Go template support