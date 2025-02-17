// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import {rehypeHeadingIds} from "@astrojs/markdown-remark";
import rehypeAutolinkHeadings from "rehype-autolink-headings";

// https://astro.build/config
export default defineConfig({
	site: 'https://astronaut.github.io',
	base: 'kidk/aikido-docs-test-2',
	integrations: [
		starlight({
			title: 'Aikido Docs',
			customCss: [
				// Load this additional CSS file using its relative path.
        		'./src/styles/headings.css',
			],
			social: {
				github: 'https://github.com/withastro/starlight',
			},
		}),
	],
	markdown: {
	    rehypePlugins: [
			rehypeHeadingIds,
			[
		        rehypeAutolinkHeadings,
		        {
		          // Wrap the heading text in a link.
		          behavior: 'wrap',
		        },
	      	],
		],
	},
});
