export type Tool = {
  slug: string;
  title: string;
  icon: string;   // nombre del icono lucide
  desc?: string;
};

export type Category = {
  slug: string;   // 'pdf', 'video', ...
  title: string;
  icon: string;   // icono lucide
  tools: Tool[];
};

export const CATEGORIES: Category[] = [
  {
    slug: 'pdf', title: 'PDF', icon: 'FileText',
    tools: [
      { slug: 'merge',        title: 'Merge PDF',       icon: 'combine' },
      { slug: 'split',        title: 'Split PDF',       icon: 'Split' },
      { slug: 'pdf-to-word',  title: 'PDF to Word',     icon: 'FileType2' },
      { slug: 'word-to-pdf',  title: 'Word to PDF',     icon: 'File' }
    ]
  },
  {
    slug: 'video', title: 'Video', icon: 'Film',
    tools: [
      { slug: 'convert',      title: 'Convert',         icon: 'Repeat' },
      { slug: 'compress',     title: 'Compress',        icon: 'Archive' },
      { slug: 'extract-audio',title: 'Extract Audio',   icon: 'Music' },
      { slug: 'merge',        title: 'Merge Video',     icon: 'Combine' }
    ]
  },
  {
    slug: 'audio', title: 'Audio', icon: 'Music',
    tools: [
      { slug: 'convert',      title: 'Convert',         icon: 'Repeat' },
      { slug: 'trim',         title: 'Trim',            icon: 'Scissors' },
      { slug: 'merge',        title: 'Merge',           icon: 'Combine' },
      { slug: 'bitrate',      title: 'Change Bitrate',  icon: 'SlidersHorizontal' }
    ]
  },
  {
    slug: 'images', title: 'Images', icon: 'Image',
    tools: [
      { slug: 'convert',      title: 'Convert',         icon: 'Repeat' },
      { slug: 'compress',     title: 'Compress',        icon: 'Archive' },
      { slug: 'resize',       title: 'Resize',          icon: 'Maximize2' },
      { slug: 'image-to-pdf', title: 'Image to PDF',    icon: 'File' }
    ]
  },
  {
    slug: 'text', title: 'Text/Docs', icon: 'FileText',
    tools: [
      { slug: 'docx-to-txt',  title: 'DOCX to TXT',     icon: 'FileType2' },
      { slug: 'txt-to-pdf',   title: 'TXT to PDF',      icon: 'File' },
      { slug: 'merge-text',   title: 'Merge Text',      icon: 'Combine' },
      { slug: 'extract-text-pdf', title: 'Extract Text from PDF', icon: 'ScanText' }
    ]
  },
  {
    slug: 'archives', title: 'Archives', icon: 'FileArchive',
    tools: [
      { slug: 'zip-unzip',    title: 'ZIP/Unzip',       icon: 'FileArchive' },
      { slug: 'extract-rar',  title: 'Extract RAR',     icon: 'PackageOpen' },
      { slug: 'create-zip',   title: 'Create ZIP',      icon: 'FolderPlus' },
      { slug: 'convert-archive', title: 'Convert Archive', icon: 'Repeat' }
    ]
  },
  {
    slug: 'ocr', title: 'OCR', icon: 'ScanLine',
    tools: [
      { slug: 'image-to-text', title: 'Image to Text',  icon: 'ScanText' },
      { slug: 'pdf-to-text',   title: 'PDF to Text',    icon: 'ScanText' },
      { slug: 'multi-lang',    title: 'Multi-language OCR', icon: 'Languages' },
      { slug: 'handwritten',   title: 'Handwritten OCR', icon: 'PenLine' }
    ]
  }
];
