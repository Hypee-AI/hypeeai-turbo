import config from '@repo/shadcn-ui/tailwind.config';

const contents = ['node_modules/@rumsan/ui/src/components/**/*.{ts,tsx}'];

config.content.push(...contents);

export default config;
