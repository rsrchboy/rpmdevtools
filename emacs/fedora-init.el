;; $Id: fedora-init.el,v 1.5 2005/10/06 16:15:15 scop Exp $

(defun fedora-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'indent-tabs-mode) nil)
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (if buffer-file-name
      (call-process "fedora-newrpmspec" nil t nil "-o" "-" buffer-file-name)
    (call-process "fedora-newrpmspec" nil t nil "-o" "-"))
  (goto-char (point-min))
  (re-search-forward "^[A-Za-z]+:\\s-*$" nil t)
  (set-buffer-modified-p nil))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'fedora-new-rpm-spec-file-init t)
