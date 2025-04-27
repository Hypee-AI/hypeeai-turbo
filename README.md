# Turbo Seed - Monorepo Template

A comprehensive monorepo template built with Turborepo for building full-stack applications using Next.js and NestJS with shadcn/ui components.

## Features

- 📦 [Turborepo](https://turbo.build/) for fast, efficient builds and dependency management
- 🎨 [shadcn/ui](https://ui.shadcn.com/) components pre-configured
- ⚛️ [Next.js](https://nextjs.org/) for frontend applications
- 🦅 [NestJS](https://nestjs.com/) for backend services
- 📚 Shared packages for common code and utilities
- 🔄 [Changesets](https://github.com/changesets/changesets) for version management
- 🧩 Typescript configured across all packages

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/en/) (v18 or higher)
- [pnpm](https://pnpm.io/) (v8 or higher)

### Installation

```bash
# Install dependencies
pnpm install
```

### Development

```bash
# Run all apps and packages in development mode
pnpm run dev

# Run a specific app or package
pnpm run dev --filter=web
pnpm run dev --filter=api
```

## Project Structure

```
.
├── apps/                   # Application code
│   ├── web/                # Next.js frontend
│   └── api/                # NestJS backend
├── packages/               # Shared packages
│   ├── sdk/                # Shared utilities and types
│   ├── eslint-config/      # ESLint configuration
│   └── typescript-config/  # TypeScript configuration
└── ...
```

## Creating New Packages

1. Create a new directory in the `packages/` folder
2. Create a `package.json` with the following structure:

```json
{
  "name": "@yourscope/package-name",
  "version": "0.0.1",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsup src/index.ts --format esm,cjs --dts",
    "dev": "tsup src/index.ts --format esm,cjs --watch --dts",
    "lint": "eslint src/",
    "clean": "rm -rf dist"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

3. Copy the `tsconfig.json` from an existing package
4. Create your source code in the `src/` directory
5. Export everything through `src/index.ts`

## Publishing Packages

This repo uses [Changesets](https://github.com/changesets/changesets) to manage versions and publishing.

```bash
# Login to npm
npm login

# Create a new changeset
pnpm changeset

# Apply changesets to update versions
pnpm changeset version

# Publish packages
pnpm changeset publish
```

> **Note:** Set `"private": true` in a package's `package.json` if you don't want to publish it to npm.

## Important Notes

- Do not modify the `eslint-config` and `typescript-config` packages unless you know what you're doing
- Always use pnpm as the package manager to maintain consistency
- Use the monorepo structure to your advantage by sharing code between applications

## License

MIT
